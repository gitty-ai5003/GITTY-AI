from typing import Optional
from datetime import datetime
from libs.shared_kernel import AggregateRoot, Identifier

class Repository(AggregateRoot):
    def __init__(
        self,
        name: str,
        root_path: str,
        language: str = "unknown",
        indexed_at: Optional[datetime] = None,
        hash: Optional[str] = None,
        id: Optional[Identifier] = None
    ):
        super().__init__(id)
        self.name = name
        self.root_path = root_path
        self.language = language
        self.indexed_at = indexed_at
        self.hash = hash
