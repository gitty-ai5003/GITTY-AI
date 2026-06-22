from pydantic import BaseModel
from typing import Optional, List

class IRImport(BaseModel):
    module: Optional[str] = None # 'user.service' in 'from user.service import UserService'
    name: str # 'UserService' or 'sys' in 'import sys'
    alias: Optional[str] = None # 'US' in 'import user_service as US'
    line_number: int
