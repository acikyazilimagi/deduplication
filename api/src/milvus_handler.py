from pymilvus import connections, Collection
import numpy as np

class MilvusHandler:

    def __init__(self, alias:str, uri: str, user: str, password: str, secure: bool):
        connections.connect(alias=alias, uri=uri, user=user, password=password, secure=secure)

        self.collection = self.load_collection("tweets")
        self.search_params = {"metric_type": "IP"}

    def load_collection(self, collection_name: str) -> Collection:
        collection = Collection(collection_name)
        collection.load()
        return collection

    def get_similar_embeddings(self, embeddings: np.ndarray):
        search_field = "example_field"
        search_params = {"metric_type":"IP"}
        search_limit = 200
        search_expr = None

        similar_embeddings = self.collection.search(embeddings, search_field, param=search_params, limit=search_limit, expr=search_expr)
        return similar_embeddings

    def disconnect(self):
        connections.disconnect("default")
