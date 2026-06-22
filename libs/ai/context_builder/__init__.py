from typing import List, Dict, Any

class ContextBuilder:
    """
    Assembles code context strings from retrieved node files, class definitions, and calls relationships.
    """
    def build_context(self, retrieved_elements: List[Dict[str, Any]]) -> str:
        context_parts = []
        for element in retrieved_elements:
            context_parts.append(
                f"Element: {element.get('name')} ({element.get('type')})\n"
                f"Source:\n{element.get('context')}\n"
                f"---"
            )
        return "\n".join(context_parts)
