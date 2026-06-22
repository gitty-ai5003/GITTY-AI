from typing import Dict, Any
from .base_agent import BaseAgent

class RepositoryQAAgent(BaseAgent):
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(input_data):
            return {"status": "error", "message": "Invalid context"}
        context = self.prepare_context(input_data)
        return {
            "status": "success",
            "agent": "RepositoryQAAgent",
            "answer": f"Mock Q&A response referencing context: {list(context.keys())}"
        }

    def validate(self, input_data: Dict[str, Any]) -> bool:
        return "query" in input_data

    def prepare_context(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"retrieved_nodes": [], "query": input_data["query"]}
