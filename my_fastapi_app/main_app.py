import uvicorn
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse, Response, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from db import database as db
from models import File
from detect import main_task
from fastapi.staticfiles import StaticFiles
import requests
from config import RSA_API, regions

app = FastAPI(docs_url="/model-api")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешение всех источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешение всех методов
    allow_headers=["*"],  # Разрешение всех заголовков
)


@app.get("/", tags=["Root"])
async def get_index():
    # Замените "index.html" на путь к вашему файлу HTML
    return FileResponse("./templates/index.html")


@app.post("/api/v1/public/detection/application/create", tags=["Working with the application"])
def create_application():
    new_application = db.Application.create()
    return {"applicationId": new_application.id}


@app.post("/api/v1/public/detection/{applicationId}/file", tags=["Working with the application"])
def download_file(applicationId: int, fileBase64: File):
    status = db.Application.get(db.Application.id == applicationId).status
    if status == 0:
        (db.Application.update(file=fileBase64.fileBase64).where(db.Application.id == applicationId)).execute()
        return Response(status_code=201, content="The file has been successfully uploaded", media_type="text/plain")
    else:
        return {"System message": f"status={status}. A file can only be uploaded to an application with status 0"}


@app.post("/api/v1/public/detection/{applicationId}/send", tags=["Working with the application"])
async def send_application(background_tasks: BackgroundTasks, applicationId: int):
    ### Status 0 - черновик
    ### Status 1 - в обработке
    ### Status 2 - успешно завершен
    ### Status 3 - завершен с ошибкой
    status = db.Application.get(db.Application.id == applicationId).status
    if status == 0:
        background_tasks.add_task(main_task, applicationId)
        (db.Application.update(status=1).where(db.Application.id == applicationId)).execute()
        return {"System message": "status=1. The request has been accepted and image processing has begun."}
    else:
        return {"System message": f"status={status}. Only a request with status 0 can be sent for processing"}


@app.get("/api/v1/public/detection/{applicationId}/status", tags=["Working with the application"])
def get_status(applicationId: int):
    # Берем статус из заявки и возвращаем
    status = (db.Application.select(db.Application.status).where(db.Application.id == applicationId))[0].status
    return {"status": status}


@app.get("/api/v1/public/detection/{applicationId}/result", tags=["Working with the application"])
def get_result(applicationId: int):
    status = db.Application.select(db.Application.status).where(db.Application.id == applicationId)[0].status
    if status == 0:
        return Response(status_code=200, content="It's impossible to get results. The file is in draft status.",
                        media_type="text/plain")
    if status == 1:
        return Response(status_code=200, content="It's impossible to get results. The file is in process.",
                        media_type="text/plain")
    if status == 2:
        row = db.Application.get(db.Application.id == applicationId)
        result_of_detect = {
            "isCar": row.isCar,
            "result": row.result
        }
        return JSONResponse(status_code=200, content=result_of_detect)
    if status == 3:
        return JSONResponse(status_code=200, content={"result": f"The process was terminated with an error, try again"})


@app.get("/api/v1/public/detection/{applicationId}/prices", tags=["Detail's prices"])
def get_prices(report_date: str,
               catalog_number: str,
               rf_subject: int,
               car_brand):
    # берем название субъекта из нашего справочника
    rf_subject = regions[f"{rf_subject}"]

    # получаем справочник субъектов РФ
    get_rf_subject_ids_result = requests.get(RSA_API['get_rf_subject_ids'].format(report_date))
    subjects = {row['subjectName']: row['subjectRF'] for row in get_rf_subject_ids_result.json()}

    # получаем cписок марок автомобилей
    get_oem_ids_result = requests.get(RSA_API['get_oem_ids'].format(report_date))
    brands = {row['name']: row['id'] for row in get_oem_ids_result.json()}

    # получаем цены на запчасть
    request_data = {
        'oemId': brands[car_brand],
        'subjectRF': subjects[rf_subject],
        'versionDate': report_date,
        'partNumber1': catalog_number
    }
    get_price_url_result = requests.post(RSA_API['get_price_url'], json=request_data)
    spare_info = get_price_url_result.json()['repairPartDtoList'][0]

    if spare_info['found']:
        return {
            'spare_name': spare_info['spareName'],
            'reg_coef': spare_info['regCoef'],
            'spare_price': spare_info['sparePrice'],
            'base_cost': spare_info['baseCost']
        }


if __name__ == '__main__':
    uvicorn.run(app, port=8001)
