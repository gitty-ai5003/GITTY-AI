from pydantic import BaseModel, Field
from typing import Dict, Any

class FileNode(BaseModel):
    id: str
    type: str = "File"
    name: str
    path: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
