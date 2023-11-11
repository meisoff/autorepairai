import onnx
import numpy as np
import onnxruntime as ort
from PIL import Image
import cv2
import matplotlib.pyplot as plt


# model_path = './models/classfication_car.onnx'
model_path = './models/model_car.onnx'
model = onnx.load(model_path)
session = ort.InferenceSession(model.SerializeToString())

# labels = ["Car", "Nocar"]
labels = ['4x4 (Нива) I (1977—2019)',
 '4x4 (Нива) I рестайлинг (2019—2023)',
 'Granta  I рестайлинг (2018—2023)',
 'Granta I (2011—2018)',
 'Kalina I (2004—2013)',
 'Kalina II (2013—2018)',
 'Largus I (2012—2023)',
 'Largus I рестайлинг (2021—2023)',
 'Niva Travel I рестайлинг (2020—2023)',
 'Priora I (2007—2013)',
 'Priora I рестайлинг (2013—2018)',
 'Vesta Cross I (2017—2023)',
 'Vesta I (2015—2023)',
 'XRAY Cross I (2018—2023)',
 'XRAY I (2015—2023)']


def get_image(path, show=False):
    with Image.open(path) as img:
        img = np.array(img.convert('RGB'))
    if show:
        plt.imshow(img)
        plt.axis('off')
    return img
# # Для обнаружения типа авто или нет
# def preprocess(img):
#     img = img / 255.
#     img = cv2.resize(img, (640, 640))
#     img = (img - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
#     img = np.transpose(img, axes=[2, 0, 1])
#     img = img.astype(np.float32)
#     img = np.expand_dims(img, axis=0)
#     return img

# Для обнаружения модели авто
def preprocess(img):
    img = img / 255.
    img = cv2.resize(img, (256, 256))
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


img_path = 'C:\\Users\\Александр\\PycharmProjects\\autorepairai_2\\parser_autoru\\new\\Largus\\I рестайлинг (2021—2023)\\img_39.png'
predict(img_path)



