from abc import ABC, abstractmethod
from typing import Dict, Any

class IRepositoryScanner(ABC):
    @abstractmethod
    def clone_or_fetch(self, repo_url: str, dest_path: str) -> str:
        """Clones a remote git repository or fetches/pulls the latest changes."""
        pass
