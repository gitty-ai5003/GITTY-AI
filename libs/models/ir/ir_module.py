from pydantic import BaseModel
from typing import List
from .ir_import import IRImport
from .ir_class import IRClass
from .ir_function import IRFunction
from .ir_call import IRCall

class IRModule(BaseModel):
    file_path: str
    language: str
    imports: List[IRImport] = []
    classes: List[IRClass] = []
    functions: List[IRFunction] = [] # top-level functions
    calls: List[IRCall] = [] # top-level calls
