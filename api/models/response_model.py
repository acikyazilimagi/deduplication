from pydantic import BaseModel

class Response(BaseModel):
    #status: str
    model_name: str
    is_duplicate: bool
