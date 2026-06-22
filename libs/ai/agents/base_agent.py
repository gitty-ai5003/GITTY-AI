from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    @abstractmethod
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Runs the agent execution logic."""
        pass

    @abstractmethod
    def validate(self, input_data: Dict[str, Any]) -> bool:
        """Validates incoming parameters/context."""
        pass

    @abstractmethod
    def prepare_context(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepares structural query contexts."""
        pass
