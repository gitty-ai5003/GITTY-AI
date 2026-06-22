from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class RepositoryModel(BaseModel):
    id: str = Field(..., description="Unique ID of the repository, typically generated from name/owner or URL hash")
    name: str = Field(..., description="Name of the repository")
    owner: str = Field(..., description="Owner of the repository")
    url: str = Field(..., description="Clone URL of the repository")
    default_branch: str = Field(default="main")
    last_indexed_at: Optional[datetime] = Field(default=None)
    status: str = Field(default="queued", description="Status: queued, indexing, completed, failed")
    metadata: Dict[str, Any] = Field(default_factory=dict)
