from typing import Optional
from libs.shared_kernel import BaseEntity, Identifier

class Directory(BaseEntity):
    def __init__(
        self,
        repository_id: Identifier,
        path: str,
        id: Optional[Identifier] = None
    ):
        super().__init__(id)
        self.repository_id = repository_id
        self.path = path
