from pydantic import BaseModel

class File(BaseModel):
    fileBase64: str

class UserInfo(BaseModel):
    login: str
    password: str

class AutoInfo(BaseModel):
    mark: str
    model: str
    year: str

class DamageInfo(BaseModel):
    damageList: list