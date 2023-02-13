from pydantic import BaseModel

class Request(BaseModel):
    text: str
