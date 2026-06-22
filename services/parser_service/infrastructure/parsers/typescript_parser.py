from ...domain.interfaces.parser import IParser
from typing import Dict, Any

class TypescriptParser(IParser):
    def parse_file(self, file_content: str) -> Dict[str, Any]:
        raise NotImplementedError("TypescriptParser is not implemented yet in Phase 2.")
Class = TypescriptParser
