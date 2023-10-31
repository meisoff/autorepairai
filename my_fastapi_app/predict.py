import onnx
import numpy as np
import onnxruntime as ort
from PIL import Image
import cv2
import matplotlib.pyplot as plt


model_path = './models/classfication_car.onnx'
model = onnx.load(model_path)
session = ort.InferenceSession(model.SerializeToString())

labels = ["Car", "Nocar"]

def get_image(path, show=False):
    with Image.open(path) as img:
        img = np.array(img.convert('RGB'))
    if show:
        plt.imshow(img)
        plt.axis('off')
    return img

def preprocess(img):
    img = img / 255.
    img = cv2.resize(img, (640, 640))
    img = (img - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
    img = np.transpose(img, axes=[2, 0, 1])
    img = img.astype(np.float32)
    img = np.expand_dims(img, axis=0)
    return img

def predict(path):
    img = get_image(path, show=True)
    img = preprocess(img)
    ort_inputs = {session.get_inputs()[0].name: img}
    preds = session.run(None, ort_inputs)[0]
    preds = np.squeeze(preds)
    a = np.argsort(preds)[::-1]
    print('class=%s ; probability=%f' %(labels[a[0]],preds[a[0]]))


img_path = '../1.jpeg'
predict(img_path)



