from typing import Dict, Any
from .base_agent import BaseAgent

class DeadCodeAgent(BaseAgent):
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        context = self.prepare_context(input_data)
        return {
            "status": "success",
            "agent": "DeadCodeAgent",
            "unreferenced_functions": []
        }

    def validate(self, input_data: Dict[str, Any]) -> bool:
        return True

    def prepare_context(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"scan_scope": input_data.get("scan_scope", "all")}
