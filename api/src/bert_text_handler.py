from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize
from config import *
import numpy as np
import torch


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

    def text_to_embedding(self, text: str) -> np.ndarray:

        text = [text]

        embeddings = self.model.encode(text)
        embeddings = normalize(embeddings)

        return embeddings
