from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import FastAPI, HTTPException, Header, Depends
from src.bert_text_handler import BertTextHandler
from src.milvus_handler import MilvusHandler
from models.response_model import Response
from models.entry_model import Entry
from config import *
import uvicorn

app = FastAPI()
security_scheme = HTTPBearer()
text_handler = BertTextHandler()


def validate_api_key(credentials: HTTPAuthorizationCredentials = Depends(security_scheme)):
    api_key = credentials.credentials

    if api_key != DEDUPLICATION_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid authorization token")


@app.get("/health-check")
def health_check():
    return {"status": "healthy"}


@app.get("/is-duplicate")
async def is_duplicate(entry: Entry, api_key: str = Depends(validate_api_key)) -> Response:
    try:
        entry_text = str(entry)

        entry_embeddings = text_handler.text_to_embedding(entry_text)

        _is_duplicate = None
        with MilvusHandler() as milvus_handler:
            similar_embeddings = milvus_handler.get_similar_embeddings(entry_embeddings)
            _is_duplicate = text_handler.is_duplicate(similar_embeddings, entry.threshold)
            milvus_handler.insert_entry(entry.entry_id, entry_embeddings)

        return Response(model_name=MODEL_NAME, is_duplicate=_is_duplicate)

    except Exception as ex:
        raise HTTPException(status_code=500, detail=(str(ex)))


if __name__ == "__main__":
    uvicorn.run(app)
