from typing import Dict, Any
from .base_agent import BaseAgent

class ImpactAgent(BaseAgent):
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(input_data):
            return {"status": "error", "message": "Missing changed_component"}
        context = self.prepare_context(input_data)
        return {
            "status": "success",
            "agent": "ImpactAgent",
            "impacted_files": [],
            "blast_radius_depth": 0
        }

    def validate(self, input_data: Dict[str, Any]) -> bool:
        return "changed_component" in input_data

    def prepare_context(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"target": input_data["changed_component"]}
