from abc import ABC, abstractmethod
from typing import Callable, Any

class IEventBus(ABC):
    @abstractmethod
    def publish(self, topic: str, event: Any) -> None:
        """Publishes an event to a specific topic/routing key."""
        pass

    @abstractmethod
    def subscribe(self, queue_name: str, topic: str, handler: Callable[[Any], None]) -> None:
        """Subscribes a handler to a queue for a specific topic/routing key."""
        pass

    @abstractmethod
    def start_consuming(self) -> None:
        """Starts the event consumer blocking loop."""
        pass
