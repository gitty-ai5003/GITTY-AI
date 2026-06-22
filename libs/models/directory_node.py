from pydantic import BaseModel, Field
from typing import Dict, Any

class DirectoryNode(BaseModel):
    id: str
    type: str = "Directory"
    name: str
    path: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
