import uvicorn
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse, Response, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from my_fastapi_app.db import database as db
from models import File
from detect import main_task
from fastapi.staticfiles import StaticFiles


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
        (db.Application.update(file=fileBase64.fileBase64).where(db.Application.id==applicationId)).execute()
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
        return Response(status_code=200, content="It's impossible to get results. The file is in draft status.", media_type="text/plain")
    if status == 1:
        return Response(status_code=200, content="It's impossible to get results. The file is in process.", media_type="text/plain")
    if status == 2:
        row = db.Application.get(db.Application.id == applicationId)
        result_of_detect = {
            "isCar": row.isCar,
            "result": row.result
        }
        return JSONResponse(status_code=200, content=result_of_detect)
    if status == 3:
        return JSONResponse(status_code=200, content={"result": f"The process was terminated with an error, try again"})



if __name__ == '__main__':
    uvicorn.run(app, port=8001)