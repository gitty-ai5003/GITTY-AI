from typing import Any, Optional
from .identifier import Identifier

class BaseEntity:
    def __init__(self, id: Optional[Identifier] = None):
        self.id = id or Identifier()

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BaseEntity):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
