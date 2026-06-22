from pydantic import BaseModel, Field
from typing import Dict, Any

class FunctionNode(BaseModel):
    id: str
    type: str = "Function"
    name: str
    path: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
