from pydantic import BaseModel
from typing import List, Optional, Any
from .ir_call import IRCall

class IRFunction(BaseModel):
    name: str
    parameters: List[str] = []
    return_type: Optional[str] = None
    start_line: int
    end_line: int
    decorators: List[str] = []
    calls: List[IRCall] = []
    is_method: bool = False
    class_context: Optional[str] = None # Name of class if this is a method
