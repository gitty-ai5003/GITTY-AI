from pydantic import BaseModel, Field
from typing import Dict, Any

class ClassNode(BaseModel):
    id: str
    type: str = "Class"
    name: str
    path: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
