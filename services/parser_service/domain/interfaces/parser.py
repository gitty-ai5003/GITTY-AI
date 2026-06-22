from abc import ABC, abstractmethod
from typing import Dict, Any

class IParser(ABC):
    @abstractmethod
    def parse_file(self, file_content: str) -> Dict[str, Any]:
        """Parses a file's content and returns a language-agnostic intermediate representation (IR)."""
        pass
