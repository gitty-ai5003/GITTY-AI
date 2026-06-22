from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class BaseEvent(BaseModel):
    event_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    version: str

class RepositoryDiscoveredV1(BaseEvent):
    repository_id: str
    name: str
    root_path: str
    url: Optional[str] = None
    version: str = Field(default="v1")

class RepositoryIndexedV1(BaseEvent):
    repository_id: str
    repository_url: str
    indexed_files_count: int
    status: str # "success", "failed"
    error_message: Optional[str] = None
    version: str = Field(default="v1")

class GraphBuiltV1(BaseEvent):
    repository_id: str
    nodes_created: int
    edges_created: int
    duration_ms: int
    version: str = Field(default="v1")

class EmbeddingCreatedV1(BaseEvent):
    repository_id: str
    chunk_id: str
    model_name: str
    vector_dimensions: int
    version: str = Field(default="v1")

class DeadCodeDetectedV1(BaseEvent):
    repository_id: str
    dead_functions: List[str] = Field(default_factory=list)
    version: str = Field(default="v1")

class VulnerabilityFoundV1(BaseEvent):
    repository_id: str
    cve_id: str
    cwe_id: str
    file_path: str
    line_number: int
    severity: str # "LOW", "MEDIUM", "HIGH", "CRITICAL"
    version: str = Field(default="v1")
