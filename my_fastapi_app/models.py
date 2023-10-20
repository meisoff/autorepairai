from pydantic import BaseModel

class File(BaseModel):
    fileBase64: str