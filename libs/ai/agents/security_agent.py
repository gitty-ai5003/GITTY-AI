from typing import Dict, Any
from .base_agent import BaseAgent

class SecurityAgent(BaseAgent):
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(input_data):
            return {"status": "error", "message": "Missing file_path"}
        context = self.prepare_context(input_data)
        return {
            "status": "success",
            "agent": "SecurityAgent",
            "findings": []
        }

    def validate(self, input_data: Dict[str, Any]) -> bool:
        return "file_path" in input_data

    def prepare_context(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"file_path": input_data["file_path"]}
