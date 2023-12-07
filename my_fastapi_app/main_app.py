import json
import uvicorn
from fastapi import FastAPI, BackgroundTasks, HTTPException, Header, Depends
from fastapi.responses import JSONResponse, Response, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from db import database as db
from models import File, UserInfo, AutoInfo
from detect import main_task
from fastapi.staticfiles import StaticFiles
from config import for_parsing
from get_prices import get_price
from validate import validate_email, validate_password
from fastapi.security import APIKeyHeader
import hashlib
from fastapi.openapi.utils import get_openapi

app = FastAPI(docs_url="/model-api")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешение всех источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешение всех методов
    allow_headers=["*"],  # Разрешение всех заголовков
)

security_definitions = {
    "APIKeyHeader": {
        "type": "apiKey",
        "name": "X-API-Key",
        "in": "header"
    }
}

api_key_dependency = APIKeyHeader(name="X-API-Key")


# Зависимость для проверки API-ключа
async def verify_api_key(api_key: str = Depends(api_key_dependency)):
    if not db.Account.select().where(db.Account.userGuid == api_key):
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key


# Добавляем Security Definitions в OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Autorepairai API",
        version="0.1.0",
        description="API for detect damaged detail and get prices",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = security_definitions
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.post("/api/v1/public/account/register", tags=["Account"])
async def register(user_info: UserInfo):
    login = user_info.login
    password = user_info.password
    try:
        flag_log, reason_log = validate_email(login)
    except:
        raise HTTPException(status_code=500, detail="System message: Unknown Error. Try again later")

    if flag_log:
        flag_pass, reason_pass = validate_password(password)
        if flag_pass:
            for_reg = login + password
            for_reg = for_reg[5:] + for_reg[:5]
            userGuid = str(hashlib.sha1(for_reg.encode('utf-8')).hexdigest())
            db.Account.create(login=login, password=password, userGuid=userGuid)
            return {"userGuid": f"{userGuid}"}
        else:
            text = f"System message: {';'.join(reason_pass)}"
            raise HTTPException(status_code=400, detail=text)
    else:
        raise HTTPException(status_code=400, detail=f"System message: {reason_log}")


@app.get("/", include_in_schema=False)
async def get_index():
    return RedirectResponse(url="/model-api")

@app.post("/api/v1/public/account/auth", tags=["Account"])
def authorization(user_info: UserInfo):
    login = user_info.login
    password = user_info.password
    try:
        login_row = db.Account.select().where(db.Account.login == login)[0]
    except:
        raise HTTPException(500, "System message Unknown Error. Try again later")


    if login_row:
        if login_row.password == password:
            userGuid = login_row.userGuid
            return {"userGuid": f"{userGuid}"}
        else:
            raise HTTPException(400, "System message: Неверный пароль")
    else:
        raise HTTPException("System message: Пользователь не зарегистрирован")


@app.post("/api/v1/public/detection/application/create", tags=["Working with the application"])
async def create_application(dependencies=Depends(verify_api_key)):
    account_id = db.Account.select().where(db.Account.userGuid == dependencies)[0].id
    new_application = db.Application.create(account_id=account_id)
    return {"applicationId": new_application.id}


@app.post("/api/v1/public/detection/{applicationId}/file", tags=["Working with the application"])
def download_file(applicationId: int, fileBase64: File, dependencies=Depends(verify_api_key)):
    status = db.Application.get(db.Application.id == applicationId).status
    if status == 0:
        (db.Application.update(file=fileBase64.fileBase64).where(db.Application.id == applicationId)).execute()
        return Response(status_code=201, content="The file has been successfully uploaded", media_type="text/plain")
    else:
        return {"System message": f"status={status}. A file can only be uploaded to an application with status 0"}


@app.post("/api/v1/public/detection/{applicationId}/send", tags=["Working with the application"])
async def send_application(background_tasks: BackgroundTasks, applicationId: int, dependencies=Depends(verify_api_key)):
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
def get_status(applicationId: int, dependencies=Depends(verify_api_key)):
    # Берем статус из заявки и возвращаем
    status = (db.Application.select(db.Application.status).where(db.Application.id == applicationId))[0].status
    return {"status": status}

@app.patch("/api/v1/public/detection/{applicationId}/auto_info", tags=["Working with the application"])
async def update_auto_info(applicationId: int, autoInfo: AutoInfo, dependencies=Depends(verify_api_key)):
    status = db.Application.get(db.Application.id == applicationId).status
    if status != 3:
        (db.Application.update(mark=autoInfo.mark, model=autoInfo.model, year=autoInfo.year).where(db.Application.id == applicationId)).execute()
        return {"System message": "Application auto info updated."}
    else:
        return {"System message": f"status={status}. Just try create new application"}


@app.get("/api/v1/public/detection/{applicationId}/result", tags=["Working with the application"])
def get_result(applicationId: int, dependencies=Depends(verify_api_key)):
    status = db.Application.select(db.Application.status).where(db.Application.id == applicationId)[0].status
    if status == 0:
        return Response(status_code=200, content="It's impossible to get results. The file is in draft status.",
                        media_type="text/plain")
    if status == 1:
        return Response(status_code=200, content="It's impossible to get results. The file is in process.",
                        media_type="text/plain")
    if status == 2:
        k = db.Application.get(db.Application.id == applicationId)

        prices = k.prices.encode('utf-8').decode('unicode_escape') if k.prices else None
        result_of_detect = {
            "mark": k.mark,
            "model": k.model,
            "year": k.year,
            "isCar": k.isCar,
            "boxes": k.result,
            "prices": prices,
        }
        return JSONResponse(status_code=200, content=result_of_detect)
    if status == 3:
        return JSONResponse(status_code=200, content={"result": f"The process was terminated with an error, try again"})


@app.get("/api/v1/public/detection/application/history", tags=["Working with the application"])
def get_histrory_application(dependencies=Depends(verify_api_key)):
    user_id = db.Account.select().where(db.Account.userGuid == dependencies)[0].id
    result = db.Application.select().where((db.Application.account_id == user_id) & (db.Application.status == 2))
    all_result = []
    for i, k in enumerate(result):
        prices = k.prices.encode('utf-8').decode('unicode_escape')
        all_result.append(
            {
                "mark": k.mark,
                "model": k.model,
                "year": k.year,
                "isCar": k.isCar,
                "boxes": k.result,
                "prices": prices,
                "index": i
            }
        )
    return all_result


@app.get("/api/v1/public/detection/{applicationId}/list_prices", tags=["Detail's prices"])
def get_prices_list(applicationId: int, report_date: str, rf_subject: int, dependencies=Depends(verify_api_key)):
    status = db.Application.select(db.Application.status).where(db.Application.id == applicationId)[0].status
    if status == 0:
        return Response(status_code=200, content="It's impossible to get prices. The file is in draft status.",
                        media_type="text/plain")
    if status == 1:
        return Response(status_code=200, content="It's impossible to get prices. The file is in process.",
                        media_type="text/plain")
    if status == 2:
        row = db.Application.get(db.Application.id == applicationId)
        list_of_prices = []
        if row.prices:
            return JSONResponse(status_code=200, content=json.loads(row.prices))
        else:
            row = db.Application.get(db.Application.id == applicationId)
            labels = json.loads(row.result)["classes"]
            if len(labels) and row.model:
                for i in labels:
                    all_prices_of_detail = []
                    for k, v in for_parsing[f"{row.model}"][i].items():
                        obj = get_price(report_date, v, rf_subject)
                        all_prices_of_detail.append({f"{k}": f"{obj['spare_price']}"})
                    list_of_prices.append(all_prices_of_detail)

                (db.Application.update(prices=json.dumps(list_of_prices)).where(
                    db.Application.id == applicationId)).execute()

                return JSONResponse(status_code=200, content=list_of_prices)

            else:
                return Response(status_code=200, content="Damage not found")

    if status == 3:
        return JSONResponse(status_code=200,
                            content={"result": f"The process was terminated with an error, try upload file again"})


@app.get("/api/v1/public/detection/prices", tags=["Detail's prices"])
def get_price_of_detail(report_date: str,
                        catalog_number: str,
                        rf_subject: int, api_key: str = Depends(verify_api_key)):
    return get_price(report_date,
                     catalog_number,
                     rf_subject)


if __name__ == '__main__':
    uvicorn.run(app, port=8001)
