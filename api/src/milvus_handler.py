from pymilvus import connections, Collection
import numpy as np
from config import *


class MilvusHandler:

    def __init__(self):
        self.collection = None

    def __enter__(self):
        connections.connect(alias=MILVUS_DB_ALIAS, host=MILVUS_DB_URI, port=MILVUS_DB_PORT)
        self.collection = Collection(MILVUS_DB_COLLECTION_NAME)
        self.collection.load()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        connections.remove_connection(MILVUS_DB_ALIAS)

    def get_similar_embeddings(self, embeddings: np.ndarray):
        search_field = MILVUS_DB_SEARCH_FIELD
        search_params = {"metric_type": "IP"}
        search_limit = MILVUS_DB_SEARCH_LIMIT
        search_expr = None

        similar_embeddings = self.collection.search(embeddings, search_field, param=search_params, limit=search_limit,
                                                    expr=search_expr, timeout=MILVUS_DB_CONNECTION_TIMEOUT)
        return similar_embeddings

    def insert_entry(self, entry_id: int, entry_embeddings: np.ndarray):
        return self.collection.insert([[entry_id], entry_embeddings], timeout=MILVUS_DB_CONNECTION_TIMEOUT)
