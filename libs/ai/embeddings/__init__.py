from abc import ABC, abstractmethod
from typing import List

class BaseEmbeddings(ABC):
    @abstractmethod
    def embed_query(self, text: str) -> List[float]:
        pass

    @abstractmethod
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        pass

class MockEmbeddings(BaseEmbeddings):
    def __init__(self, model_name: str = "bge-small"):
        self.model_name = model_name

    def embed_query(self, text: str) -> List[float]:
        # Return mock 384-dimensional vector (or similar)
        return [0.1] * 384

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [[0.1] * 384 for _ in texts]
