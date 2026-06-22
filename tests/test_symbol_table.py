import pytest
from services.parser_service.application.symbol_table import SymbolTable

def test_symbol_table_registration_and_resolution():
    st = SymbolTable()
    
    st.register_symbol("UserService", "apps.user_service.UserService")
    st.register_symbol("user_service", "apps.user_service.UserService")
    
    # Test direct resolution
    assert st.resolve_symbol("UserService") == "apps.user_service.UserService"
    assert st.resolve_symbol("user_service") == "apps.user_service.UserService"
    
    # Test nested sub-attribute resolution
    assert st.resolve_symbol("user_service.login") == "apps.user_service.UserService.login"
    assert st.resolve_symbol("UserService.create") == "apps.user_service.UserService.create"
    
    # Test unresolved symbols
    assert st.resolve_symbol("DatabaseClient") is None
    assert st.resolve_symbol("db.query") is None

def test_symbol_table_clear():
    st = SymbolTable()
    st.register_symbol("foo", "bar")
    assert st.resolve_symbol("foo") == "bar"
    
    st.clear()
    assert st.resolve_symbol("foo") is None
