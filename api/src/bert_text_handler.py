from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize
import numpy as np
import torch

MODEL_NAME = "loodos/bert-base-turkish-uncased" 

class BertTextHandler:

    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)

    def is_duplicate(self, similar_embeddings: np.ndarray, threshold: float) -> bool:
        embedding_similarities = similar_embeddings[0].distances

        if not embedding_similarities:
            return False

        if embedding_similarities[0] >= threshold:
            return True

        return False

    def text_to_embedding(self, text: list[str]) -> np.ndarray:
        if type(text) == str:
            text = [text]
        elif type(text[0]) == str:
            pass
            
        embeddings = self.model.encode(text)
        embeddings = normalize(embeddings)

        return embeddings
