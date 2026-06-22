from pydantic import BaseModel, Field
from typing import Dict, Any

class ImportNode(BaseModel):
    id: str
    type: str = "Import"
    name: str
    path: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
