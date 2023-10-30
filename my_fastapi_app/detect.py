import time
from io import BytesIO

from my_fastapi_app.classfication_car import type_of_car
from my_fastapi_app.db import database as db
from main import Detection
from PIL import Image
import numpy as np
import base64
import json


def detect_car(fileBase64):
    """
    :param fileBase64:
    :return: int
    """

    data_car = type_of_car(fileBase64)

    return data_car


    #TODO: добавить модель классификации изображения


def detect_damage(fileBase64):
    try:
        detection = Detection(
            model_path='best.onnx',
            classes=['damaged door', 'damaged window', 'damaged headlight', 'damaged mirror', 'dent', 'damaged hood',
                     'damaged bumper', 'damaged wind shield']
        )
        image = Image.open(BytesIO(base64.b64decode(fileBase64))).convert("RGB")
        image = np.array(image)
        image = image[:, :, ::-1].copy()
        results = detection(image)


        return {
            "status": 0,
            "prediction": json.dumps(results),
        }
    except:
        return {"status": 2}

def main_task(applicationId: int):
    file = (db.Application.get(db.Application.id == applicationId)).file
    result_car = detect_car(file)
    time.sleep(5)

    # result_car 0 - успешно выполнился
    # result_car 1 - на фото не найдено авто
    # result_car 2 - файл битый

    if result_car["status"] == 0:
        if result_car["typeVehicle"] != "Car":
            (db.Application.update(isCar=False, status=2, result="AUTOREPAIR.BAD_RESULT: Car not found").where(
                db.Application.id == applicationId)).execute()
        else:
            (db.Application.update(isCar=True).where(db.Application.id == applicationId)).execute()
            result_damage = detect_damage(file)
            # result_damage == 0 (дефекты обнаружены)
            # result_damage == 1 (дефекты не обнаружены)
            # result_damage == 2 (файл битый)


            if result_damage["status"] == 0:
                (db.Application.update(status=2, result=result_damage["prediction"]).where(
                    db.Application.id == applicationId)).execute()

            if result_damage["status"] == 1:
                (db.Application.update(status=2, result=result_damage["prediction"]).where(
                    db.Application.id == applicationId)).execute()


    if result_car["status"] == 1:
        (db.Application.update(status=3, result="AUTOREPAIR.FILELIB: File problem").where(
            db.Application.id == applicationId)).execute()