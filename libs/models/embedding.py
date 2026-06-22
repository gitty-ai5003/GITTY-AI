from pydantic import BaseModel, Field
from typing import List, Dict, Any

class EmbeddingModel(BaseModel):
    id: str = Field(..., description="Unique chunk / vector identifier")
    node_id: str = Field(..., description="Node ID this embedding is associated with (e.g. Function, File, Class)")
    text: str = Field(..., description="Original raw text chunk")
    vector: List[float] = Field(..., description="Floating point vector coefficients")
    model_name: str = Field(..., description="Model version/name used to generate the embedding")
    metadata: Dict[str, Any] = Field(default_factory=dict)
