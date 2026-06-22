from typing import Optional
from libs.shared_kernel import BaseEntity, Identifier

class File(BaseEntity):
    def __init__(
        self,
        repository_id: Identifier,
        path: str,
        extension: str,
        size: int,
        language: str,
        checksum: str, # sha256 checksum of the file content
        id: Optional[Identifier] = None
    ):
        super().__init__(id)
        self.repository_id = repository_id
        self.path = path
        self.extension = extension
        self.size = size
        self.language = language
        self.checksum = checksum
