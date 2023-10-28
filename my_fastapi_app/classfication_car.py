#There will be some function
from my_fastapi_app.models import File


def type_of_car(file: File.fileBase64) -> dict:

    # status 0 - успешно выполнился
    # status 1 - непредвиденная ошибка

    return {
        "status": 0,
        "typeVehicle": 0
    }
