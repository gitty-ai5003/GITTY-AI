from typing import Dict
from ..domain.interfaces.parser import IParser
from ..infrastructure.parsers.python_parser import PythonParser
from ..infrastructure.parsers.java_parser import JavaParser
from ..infrastructure.parsers.javascript_parser import JavascriptParser
from ..infrastructure.parsers.typescript_parser import TypescriptParser

class ParserFactory:
    def __init__(self):
        self._parsers: Dict[str, IParser] = {
            "python": PythonParser(),
            "java": JavaParser(),
            "javascript": JavascriptParser(),
            "typescript": TypescriptParser()
        }

    def get_parser(self, language: str) -> IParser:
        normalized = language.lower()
        if normalized not in self._parsers:
            raise ValueError(f"No parser implementation registered for language: {language}")
        return self._parsers[normalized]
