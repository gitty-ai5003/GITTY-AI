from typing import Dict, Any

class PromptTemplate:
    def __init__(self, template: str):
        self.template = template

    def format(self, **kwargs: Any) -> str:
        return self.template.format(**kwargs)

# Predefined prompts for Graph queries & Cypher validation
CYPHER_GENERATION_PROMPT = PromptTemplate(
    "Given the database schema below, generate a Neo4j Cypher query to answer the user request:\n"
    "Schema: {schema}\n"
    "Request: {request}\n"
    "Cypher Query:"
)

CODE_EXPLANATION_PROMPT = PromptTemplate(
    "Explain the following code snippet from the repository:\n"
    "Path: {path}\n"
    "Code:\n{code}\n"
    "Explanation:"
)
