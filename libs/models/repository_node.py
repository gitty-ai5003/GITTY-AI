from pydantic import BaseModel, Field
from typing import Dict, Any

class RepositoryNode(BaseModel):
    id: str
    type: str = "Repository"
    name: str
    path: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
