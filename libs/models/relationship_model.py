from pydantic import BaseModel, Field
from typing import Dict, Any

class RelationshipModel(BaseModel):
    id: str
    source_node: str # source node ID
    target_node: str # target node ID
    relationship_type: str # CONTAINS, IMPORTS, CALLS, etc.
    metadata: Dict[str, Any] = Field(default_factory=dict)
