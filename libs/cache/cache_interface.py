from abc import ABC, abstractmethod
from typing import Optional, Any

class ICache(ABC):
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        """Gets value from cache. Returns None if key doesn't exist."""
        pass

    @abstractmethod
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Sets value in cache with optional TTL in seconds."""
        pass

    @abstractmethod
    def delete(self, key: str) -> None:
        """Deletes key from cache."""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clears all cached items."""
        pass
