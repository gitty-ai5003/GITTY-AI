from ...domain.interfaces.parser import IParser
from typing import Dict, Any

class JavascriptParser(IParser):
    def parse_file(self, file_content: str) -> Dict[str, Any]:
        raise NotImplementedError("JavascriptParser is not implemented yet in Phase 2.")
Class = JavascriptParser
