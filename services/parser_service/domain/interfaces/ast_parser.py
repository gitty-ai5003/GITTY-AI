from abc import ABC, abstractmethod
from typing import Any

class IASTParser(ABC):
    @abstractmethod
    def get_ast(self, file_content: str) -> Any:
        """Parses source code into an Abstract Syntax Tree (AST) structure using Tree-sitter or native engines."""
        pass
