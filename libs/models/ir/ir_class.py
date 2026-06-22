from pydantic import BaseModel
from typing import List, Optional
from .ir_function import IRFunction

class IRClass(BaseModel):
    name: str
    bases: List[str] = [] # parent classes e.g. ['BaseService']
    start_line: int
    end_line: int
    decorators: List[str] = []
    methods: List[IRFunction] = []
