import time
from my_fastapi_app.db import database as db

from celery import Celery
import redis

redis = redis.Redis(host='localhost', port=6379, decode_responses=True)

app = Celery(
    'main_task',
    broker='redis://localhost:6379/0',  # Замените на свой брокер сообщений
    backend='redis://localhost:8001/0'  # Замените на свой бэкенд
)

def detect_car(fileBase64):
    return {
        "status": 0
    }


def detect_damage(fileBase64):
    # detection = Detection(
    #     model_path='best.onnx',
    #     classes=['damaged door', 'damaged window', 'damaged headlight', 'damaged mirror', 'dent', 'damaged hood',
    #              'damaged bumper', 'damaged wind shield']
    # )
    #
    # image = Image.open(base64.b64decode(fileBase64)).convert("RGB")
    # image = np.array(image)
    # image = image[:, :, ::-1].copy()
    # results = detection(image)

    return {
        "status": 0,
        "prediction": "text"
    }

@app.task
def main_task(applicationId):
    file = db.Application.select(db.Application.file).where(db.Application.id == applicationId)
    result_car = detect_car(file)
    time.sleep(5)

    # result_car 0 - успешно выполнился
    # result_car 1 - на фото не найдено авто
    # result_car 2 - файл битый

    if result_car["status"] == 0:
        db.Application.update(isCar=True).where(db.Application.id == applicationId)
        result_damage = detect_damage(file)
        # result_damage == 0 (дефекты обнаружены)
        # result_damage == 1 (дефекты не обнаружены)

        if result_damage["status"] == 0:
            db.Application.update(status=2, result=result_damage["prediction"]).where(
                db.Application.id == applicationId)

        if result_damage["status"] == 1:
            db.Application.update(status=2, result=result_damage["prediction"]).where(
                db.Application.id == applicationId)

    if result_car["status"] == 1:
        db.Application.update(isCar=False, status=2, result="AUTOREPAIR.BAD_RESULT: Car not found").where(
            db.Application.id == applicationId)
    if result_car["status"] == 2:
        db.Application.update(status=3, result="AUTOREPAIR.FILELIB: File problem").where(
            db.Application.id == applicationId)

