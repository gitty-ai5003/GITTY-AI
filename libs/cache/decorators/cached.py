import functools
from typing import Callable, Any
from ..memory_cache import MemoryCache

_default_cache = MemoryCache()

def cached(cache_instance=None):
    """
    Decorator to cache function results. Uses local MemoryCache by default.
    """
    cache = cache_instance or _default_cache

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Construct cache key based on function name and arguments
            key_parts = [func.__name__, str(args), str(sorted(kwargs.items()))]
            key = ":".join(key_parts)
            
            cached_val = cache.get(key)
            if cached_val is not None:
                return cached_val
                
            val = func(*args, **kwargs)
            cache.set(key, val)
            return val
        return wrapper
    return decorator
