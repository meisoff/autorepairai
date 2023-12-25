from models import File
import onnx
import onnxruntime as ort
import cv2
from io import BytesIO
from PIL import Image
import base64
import numpy as np


class DetectModelAuto:

    def __init__(self):
        self.labels_lada = ["Granta", "Largus", "Vesta", "XRAY"]
        self.labels_classification = ["Car", "Nocar"]
        self.path = {
            "classification": './models/classification_car.onnx',
            # "lada_model": 'C:\\Users\\Александр\\PycharmProjects\\autorepairai_2\\my_fastapi_app\\models\\model_lada.onnx'
        }
        self.model = None
        self.session = None
        self.img = None

    def start(self, file: File) -> dict:
        # status 0 - успешно выполнился
        # status 1 - непредвиденная ошибка

        try:
            self.initialization_model("classification", file)
            isCar = self.predict("classification")

            if isCar:
                # self.initialization_model("lada_model", file)
                # lada_model = self.predict("lada_model")

                return {
                    "isCar": True,
                    "status": 0
                }

            else:

                return {
                    "isCar": False,
                    "status": 0
                }
        except:

            return {
                "status": 1
            }

    def initialization_model(self, model, fileBase64):
        self.model = onnx.load(self.path[f"{model}"])
        self.session = ort.InferenceSession(self.model.SerializeToString())
        image = Image.open(BytesIO(base64.b64decode(fileBase64))).convert("RGB")
        image = np.array(image)
        self.preprocess(image)

    def preprocess(self, img):
        img = img / 255.
        img = cv2.resize(img, (640, 640))
        img = (img - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
        img = np.transpose(img, axes=[2, 0, 1])
        img = img.astype(np.float32)
        img = np.expand_dims(img, axis=0)
        self.img = img

    def predict(self, type):
        ort_inputs = {self.session.get_inputs()[0].name: self.img}
        preds = self.session.run(None, ort_inputs)[0]
        preds = np.squeeze(preds)
        a = np.argsort(preds)[::-1]

        if type == "classification":
            if self.labels_classification[a[0]] == "Car" and float(preds[a[0]]) > 0.7:
                return True
            else:
                return False
        else:
            if float(preds[a[0]]) > 0.5:
                return self.labels_lada[a[0]]
            else:
                return "model not defined"


