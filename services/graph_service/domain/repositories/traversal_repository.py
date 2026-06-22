from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ITraversalRepository(ABC):
    @abstractmethod
    def traverse_bfs(self, start_id: str, edge_types: List[str]) -> List[str]:
        """Performs BFS traversal starting at a node filtering by edge types."""
        pass

    @abstractmethod
    def traverse_dfs(self, start_id: str, edge_types: List[str]) -> List[str]:
        """Performs DFS traversal starting at a node filtering by edge types."""
        pass

    @abstractmethod
    def get_shortest_path(self, start_id: str, end_id: str) -> List[str]:
        """Calculates the shortest structural path between two elements."""
        pass
