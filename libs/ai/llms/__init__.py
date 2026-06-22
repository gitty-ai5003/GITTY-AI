from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str, system_prompt: str = None, options: Dict[str, Any] = None) -> str:
        pass

class MockLLM(BaseLLM):
    def __init__(self, provider: str):
        self.provider = provider

    def generate(self, prompt: str, system_prompt: str = None, options: Dict[str, Any] = None) -> str:
        return f"Mock response from {self.provider} for query: {prompt[:30]}..."
