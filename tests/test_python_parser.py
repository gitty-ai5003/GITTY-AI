import pytest
from services.parser_service.infrastructure.parsers.python_parser import PythonParser

def test_python_parser_basic_functions():
    code = """
import sys
from os import path
import math as m

@cached
def compute_sum(a, b: int) -> int:
    return a + b
"""
    parser = PythonParser()
    res = parser.parse_file(code)
    
    assert res["language"] == "python"
    
    # Assert imports
    imports = res["imports"]
    assert len(imports) == 3
    assert imports[0]["name"] == "sys"
    assert imports[1]["module"] == "os"
    assert imports[1]["name"] == "path"
    assert imports[2]["name"] == "math"
    assert imports[2]["alias"] == "m"
    
    # Assert functions
    functions = res["functions"]
    assert len(functions) == 1
    func = functions[0]
    assert func["name"] == "compute_sum"
    assert func["parameters"] == ["a", "b"]
    assert func["return_type"] == "int"
    assert "cached" in func["decorators"]
    assert not func["is_method"]

def test_python_parser_classes_and_methods():
    code = """
class BaseService:
    pass

@custom_decorator
class UserService(BaseService, api.Service):
    def __init__(self, db_client):
        self.db = db_client
        
    async def get_user(self, user_id):
        log_info("fetching user")
        return self.db.find(user_id)
"""
    parser = PythonParser()
    res = parser.parse_file(code)
    
    classes = res["classes"]
    assert len(classes) == 2
    
    # BaseService
    base_class = classes[0]
    assert base_class["name"] == "BaseService"
    assert base_class["bases"] == []
    
    # UserService
    user_class = classes[1]
    assert user_class["name"] == "UserService"
    assert user_class["bases"] == ["BaseService", "api.Service"]
    assert "custom_decorator" in user_class["decorators"]
    
    # Assert methods inside UserService
    methods = user_class["methods"]
    assert len(methods) == 2
    
    init_method = methods[0]
    assert init_method["name"] == "__init__"
    assert init_method["parameters"] == ["self", "db_client"]
    assert init_method["is_method"]
    assert init_method["class_context"] == "UserService"
    
    get_user_method = methods[1]
    assert get_user_method["name"] == "get_user"
    assert get_user_method["parameters"] == ["self", "user_id"]
    
    # Assert calls
    calls = get_user_method["calls"]
    assert len(calls) == 2
    assert calls[0]["name"] == "log_info"
    assert calls[0]["arguments"] == ["fetching user"]
    assert calls[1]["name"] == "self.db.find"
    assert calls[1]["arguments"] == ["user_id"]

def test_python_parser_syntax_error():
    code = "class UserService"  # Syntax error: missing colon
    parser = PythonParser()
    res = parser.parse_file(code)
    
    assert res["language"] == "python"
    assert res["classes"] == []
    assert res["functions"] == []
    assert res["imports"] == []

def test_python_parser_other_decorator_styles():
    code = """
@cached(ttl=10)
def process():
    pass
"""
    parser = PythonParser()
    res = parser.parse_file(code)
    functions = res["functions"]
    assert len(functions) == 1
    assert "cached" in functions[0]["decorators"]
