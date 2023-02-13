from src.bert_text_handler import BertTextHandler
from src.milvus_handler import MilvusHandler
from fastapi import FastAPI, HTTPException
from models.response_model import Response
from models.request_model import Request
from config import *
import uvicorn


app = FastAPI()
text_handler = BertTextHandler()
milvus_handler = MilvusHandler(alias=MILVUS_DB_ALIAS, uri=MILVUS_DB_URI, user=MILVUS_DB_USERNAME, password=MILVUS_DB_PASSWORD, secure=MILVUS_DB_SECURE)


@app.get("/health-check")
def health_check():
    return {"status": "healthy"}

@app.get("/is-duplicate")
async def is_duplicate(request: Request) -> Response:

    if not request.text:
        raise HTTPException(status_code=400, detail="Bad request, no text")
    
    try:
        embeddings = text_handler.text_to_embedding(request.text)
        similar_embeddings = milvus_handler.get_similar_embeddings(embeddings)
        is_duplicate = text_handler.is_duplicate(similar_embeddings, MILVUS_SEARCH_THRESHOLD)

        return Response(is_duplicate=is_duplicate)

    except Exception as ex:
        raise HTTPException(status_code=500, detail=(ex))
