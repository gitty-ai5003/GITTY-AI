from typing import TypeVar, Generic, Union, Callable, Any

T = TypeVar('T')
E = TypeVar('E')

class Result(Generic[T, E]):
    def __init__(self, is_success: bool, value: Union[T, None], error: Union[E, None]):
        self._is_success = is_success
        self._value = value
        self._error = error

    @property
    def is_success(self) -> bool:
        return self._is_success

    @property
    def is_failure(self) -> bool:
        return not self._is_success

    @property
    def value(self) -> T:
        if not self._is_success:
            raise ValueError("Cannot get value of a failed Result. Error: " + str(self._error))
        return self._value

    @property
    def error(self) -> E:
        if self._is_success:
            raise ValueError("Cannot get error of a successful Result.")
        return self._error

    @classmethod
    def ok(cls, value: T = None) -> 'Result[T, Any]':
        return cls(True, value, None)

    @classmethod
    def fail(cls, error: E) -> 'Result[Any, E]':
        return cls(False, None, error)

    def map(self, fn: Callable[[T], Any]) -> 'Result[Any, E]':
        if self.is_failure:
            return self
        return Result.ok(fn(self.value))

    def bind(self, fn: Callable[[T], 'Result[Any, E]']) -> 'Result[Any, E]':
        if self.is_failure:
            return self
        return fn(self.value)
