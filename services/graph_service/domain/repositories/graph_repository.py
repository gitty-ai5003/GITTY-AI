from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class IGraphRepository(ABC):
    @abstractmethod
    def create_database(self) -> None:
        """Initializes empty graph structures / tables."""
        pass

    @abstractmethod
    def clear_database(self) -> None:
        """Clears all nodes and edges from the graph."""
        pass

    @abstractmethod
    def get_schema_summary(self) -> Dict[str, Any]:
        """Returns node labels, relationship types, and count summaries."""
        pass
