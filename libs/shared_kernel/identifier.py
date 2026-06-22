import uuid
from typing import Any

class Identifier:
    def __init__(self, value: str = None):
        self._value = value or str(uuid.uuid4())

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Identifier):
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return self.value
