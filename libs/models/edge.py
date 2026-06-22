from pydantic import BaseModel, Field
from typing import Dict, Any

class EdgeModel(BaseModel):
    id: str = Field(..., description="Unique edge identifier")
    from_node: str = Field(..., description="Source node ID")
    to_node: str = Field(..., description="Target node ID")
    type: str = Field(..., description="Edge type e.g. CALLS, IMPORTS, DEPENDS_ON, USES")
    source: str = Field(..., description="Source of verification: 'ast' or 'llm_inferred'")
    confidence: float = Field(default=1.0, description="Confidence level between 0.0 and 1.0")
    properties: Dict[str, Any] = Field(default_factory=dict)
