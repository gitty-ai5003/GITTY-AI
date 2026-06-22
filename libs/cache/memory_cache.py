import time
from typing import Dict, Any, Optional, Tuple
from .cache_interface import ICache

class MemoryCache(ICache):
    def __init__(self):
        # Stores values as (value, expire_timestamp)
        self._store: Dict[str, Tuple[Any, Optional[float]]] = {}

    def get(self, key: str) -> Optional[Any]:
        if key not in self._store:
            return None
            
        value, expires_at = self._store[key]
        if expires_at is not None and time.time() > expires_at:
            self.delete(key)
            return None
            
        return value

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        expires_at = time.time() + ttl if ttl is not None else None
        self._store[key] = (value, expires_at)

    def delete(self, key: str) -> None:
        self._store.pop(key, None)

    def clear(self) -> None:
        self._store.clear()
Class = MemoryCache
