from io import BytesIO
from classfication_car import DetectModelAuto
from db import database as db
from main import Detection
from PIL import Image
import numpy as np
import base64
import json


def detect_damage(fileBase64):
    try:
        detection = Detection(
            model_path='models/car_damage.onnx',
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
        return {"status": 1}

def main_task(applicationId: int):
    file = (db.Application.get(db.Application.id == applicationId)).file
    result_car = DetectModelAuto.start(file)

    # result_car 0 - успешно выполнился (вернул True|False)
    # result_car 1 - не выполнился

    if result_car["status"] == 0:
        if not result_car["isCar"]:
            (db.Application.update(isCar=False, status=2, result="AUTOREPAIR.BAD_RESULT: Car not found").where(
                db.Application.id == applicationId)).execute()
        else:
            # result_damage == 0 (дефекты обнаружены)
            # result_damage == 1 (дефекты не обнаружены)
            # result_damage == 2 (файл битый)

            if result_car["model"] is not "model not defined":
                (db.Application.update(model=result_car["model"]).where(
                    db.Application.id == applicationId)).execute()

            result_damage = detect_damage(file)

            if result_damage["status"] == 0:
                (db.Application.update(status=2, isCar=True, result=result_damage["prediction"]).where(
                    db.Application.id == applicationId)).execute()

            if result_damage["status"] == 1:
                (db.Application.update(status=2, isCar=True, result=result_damage["prediction"]).where(
                    db.Application.id == applicationId)).execute()


    if result_car["status"] == 1:
        (db.Application.update(status=3,  result="AUTOREPAIR.FILELIB: File problem").where(
            db.Application.id == applicationId)).execute()
