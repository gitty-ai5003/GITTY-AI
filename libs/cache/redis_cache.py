import redis
import json
from typing import Optional, Any
from .cache_interface import ICache

class RedisCache(ICache):
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.client = redis.Redis(host=host, port=port, db=db)

    def get(self, key: str) -> Optional[Any]:
        data = self.client.get(key)
        if data is None:
            return None
        try:
            return json.loads(data.decode("utf-8"))
        except Exception:
            return data.decode("utf-8")

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        payload = json.dumps(value)
        self.client.set(key, payload, ex=ttl)

    def delete(self, key: str) -> None:
        self.client.delete(key)

    def clear(self) -> None:
        self.client.flushdb()
Class = RedisCache
