from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IFileWalker(ABC):
    @abstractmethod
    def walk(self, root_path: str) -> List[Dict[str, Any]]:
        """
        Recursively walks directories, respects ignore rules (.gitignore),
        computes sha256 checksums, and yields a list of file details:
        [{'path': ..., 'extension': ..., 'size': ..., 'checksum': ...}]
        """
        pass
