from my_fastapi_app.models import File
import onnx
import onnxruntime as ort
import cv2
from io import BytesIO
from PIL import Image
import base64
import numpy as np

model_path = './models/classfication_car.onnx'
model = onnx.load(model_path)
session = ort.InferenceSession(model.SerializeToString())

labels = ["Car", "Nocar"]


def type_of_car(file: File) -> dict:

    # status 0 - успешно выполнился
    # status 1 - непредвиденная ошибка

    try:
        result = predict(file)
        return result
    except:
        return {
            "status": 1
        }


def preprocess(img):
    img = img / 255.
    img = cv2.resize(img, (640, 640))
    img = (img - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
    img = np.transpose(img, axes=[2, 0, 1])
    img = img.astype(np.float32)
    img = np.expand_dims(img, axis=0)
    return img

def predict(fileBase64):
    image = Image.open(BytesIO(base64.b64decode(fileBase64))).convert("RGB")
    image = np.array(image)
    img = preprocess(image)
    ort_inputs = {session.get_inputs()[0].name: img}
    preds = session.run(None, ort_inputs)[0]
    preds = np.squeeze(preds)
    a = np.argsort(preds)[::-1]
    print(float(preds[a[0]]) > 0.7)
    print(float(preds[a[0]]))
    if labels[a[0]] == "Car" and float(preds[a[0]]) > 0.7:
        typeCar = True
    else:
        typeCar = False

    return {
        "status": 0,
        "isCar": typeCar
    }
