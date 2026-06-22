from pydantic import BaseModel
from typing import List, Optional

class IRCall(BaseModel):
    name: str # 'login' or 'user_service.login'
    caller_name: Optional[str] = None # class/function context name where the call happens
    line_number: int
    arguments: List[str] = []
