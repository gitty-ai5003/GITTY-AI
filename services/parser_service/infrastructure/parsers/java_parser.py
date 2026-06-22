from ...domain.interfaces.parser import IParser
from typing import Dict, Any

class JavaParser(IParser):
    def parse_file(self, file_content: str) -> Dict[str, Any]:
        raise NotImplementedError("JavaParser is not implemented yet in Phase 2.")
Class = JavaParser
