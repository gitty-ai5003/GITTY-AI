from typing import List, Optional
from .base_entity import BaseEntity
from .identifier import Identifier
from .domain_event import DomainEvent

class AggregateRoot(BaseEntity):
    def __init__(self, id: Optional[Identifier] = None):
        super().__init__(id)
        self._domain_events: List[DomainEvent] = []

    @property
    def domain_events(self) -> List[DomainEvent]:
        return self._domain_events.copy()

    def add_domain_event(self, event: DomainEvent) -> None:
        self._domain_events.append(event)

    def clear_domain_events(self) -> None:
        self._domain_events.clear()
