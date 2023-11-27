from pydantic import BaseModel

class File(BaseModel):
    fileBase64: str

class UserInfo(BaseModel):
    login: str
    password: str