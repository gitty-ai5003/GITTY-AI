from typing import List, Dict, Any
from ..domain.interfaces.file_walker import IFileWalker

class FileDiscoveryService:
    def __init__(self, file_walker: IFileWalker):
        self.file_walker = file_walker

    def discover_files(self, root_path: str) -> List[Dict[str, Any]]:
        return self.file_walker.walk(root_path)
