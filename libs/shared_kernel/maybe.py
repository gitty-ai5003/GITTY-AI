from typing import TypeVar, Generic, Union, Callable, Any

T = TypeVar('T')

class Maybe(Generic[T]):
    def __init__(self, value: Union[T, None]):
        self._value = value

    @property
    def has_value(self) -> bool:
        return self._value is not None

    @property
    def is_empty(self) -> bool:
        return self._value is None

    @property
    def value(self) -> T:
        if self._value is None:
            raise ValueError("Cannot get value from empty Maybe.")
        return self._value

    @classmethod
    def some(cls, value: T) -> 'Maybe[T]':
        if value is None:
            raise ValueError("Maybe.some() cannot take None.")
        return cls(value)

    @classmethod
    def none(cls) -> 'Maybe[Any]':
        return cls(None)

    @classmethod
    def from_value(cls, value: Union[T, None]) -> 'Maybe[T]':
        return cls(value)

    def map(self, fn: Callable[[T], Any]) -> 'Maybe[Any]':
        if self.is_empty:
            return Maybe.none()
        return Maybe.from_value(fn(self.value))

    def bind(self, fn: Callable[[T], 'Maybe[Any]']) -> 'Maybe[Any]':
        if self.is_empty:
            return Maybe.none()
        return fn(self.value)

    def get_or_else(self, default: T) -> T:
        if self.is_empty:
            return default
        return self.value
