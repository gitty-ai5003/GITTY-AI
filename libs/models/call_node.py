from pydantic import BaseModel, Field
from typing import Dict, Any

class CallNode(BaseModel):
    id: str
    type: str = "Call"
    name: str
    path: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
