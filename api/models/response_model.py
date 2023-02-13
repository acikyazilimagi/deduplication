from pydantic import BaseModel

class Response(BaseModel):
    is_duplicate: bool
