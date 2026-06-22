from abc import ABC, abstractmethod

class ILanguageDetector(ABC):
    @abstractmethod
    def detect_language(self, file_path: str) -> str:
        """Determines programming language based on file path extension/headers."""
        pass
