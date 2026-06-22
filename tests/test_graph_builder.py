import pytest
import sqlite3
import hashlib
from typing import Dict, Any, Callable
from services.graph_service.infrastructure.repositories.sqlite_graph_repository import SQLiteGraphRepository
from services.graph_service.application.graph_builder import GraphBuilder
from services.parser_service.application.symbol_table import SymbolTable
from libs.models.ir import IRModule, IRImport, IRClass, IRFunction, IRCall

class MockEventBus:
    def __init__(self):
        self.published = []

    def publish(self, topic: str, event: Any) -> None:
        self.published.append((topic, event))

    def subscribe(self, queue_name: str, topic: str, handler: Callable[[Any], None]) -> None:
        pass

    def start_consuming(self) -> None:
        pass

def test_graph_builder_success(tmp_path):
    db_path = str(tmp_path / "test_gitty_graph.db")
    repo = SQLiteGraphRepository(db_path=db_path)
    symbol_table = SymbolTable()
    event_bus = MockEventBus()
    
    builder = GraphBuilder(repository=repo, symbol_table=symbol_table, publisher=event_bus)
    
    # Create sample IR module
    modules = [
        IRModule(
            file_path="user_service.py",
            language="python",
            imports=[
                IRImport(name="sys", line_number=1),
                IRImport(module="os", name="path", line_number=2)
            ],
            classes=[
                IRClass(
                    name="UserService",
                    bases=["BaseService"],
                    start_line=4,
                    end_line=15,
                    decorators=["api_service"],
                    methods=[
                        IRFunction(
                            name="login",
                            parameters=["self", "username"],
                            return_type="bool",
                            start_line=6,
                            end_line=10,
                            decorators=[],
                            calls=[
                                IRCall(name="hash_password", line_number=8, arguments=["username"]),
                                IRCall(name="db.find", line_number=9, arguments=["username"])
                            ],
                            is_method=True,
                            class_context="UserService"
                        )
                    ]
                )
            ],
            functions=[
                IRFunction(
                    name="hash_password",
                    parameters=["password"],
                    return_type="str",
                    start_line=17,
                    end_line=19,
                    decorators=[],
                    calls=[],
                    is_method=False
                )
            ],
            calls=[]
        )
    ]
    
    repo_id = "test-repo-id"
    res = builder.build_graph(
        repo_id=repo_id,
        repo_name="test_repo",
        repo_path="/path/to/test_repo",
        modules=modules
    )
    
    assert res["nodes_created"] > 0
    assert res["edges_created"] > 0
    
    # Check published events
    assert len(event_bus.published) == 1
    topic, event = event_bus.published[0]
    assert topic == "graph.built"
    assert event.repository_id == repo_id
    assert event.nodes_created == res["nodes_created"]
    assert event.edges_created == res["edges_created"]
    
    # Verify sqlite repository tables actually contain data
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check repositories table
    cursor.execute("SELECT id, name, language FROM repositories")
    repos = cursor.fetchall()
    assert len(repos) == 1
    assert repos[0] == ("test-repo-id", "test_repo", "python")
    
    # Check nodes table
    cursor.execute("SELECT type, name FROM nodes")
    nodes = cursor.fetchall()
    node_types = {n[0] for n in nodes}
    assert "Repository" in node_types
    assert "File" in node_types
    assert "Class" in node_types
    assert "Function" in node_types
    assert "Import" in node_types
    assert "Call" in node_types
    
    # Check relationships table
    cursor.execute("SELECT relationship_type FROM relationships")
    rels = cursor.fetchall()
    rel_types = {r[0] for r in rels}
    assert "CONTAINS" in rel_types
    assert "IMPORTS" in rel_types
    assert "CALLS" in rel_types
    assert "BELONGS_TO" in rel_types
    assert "INHERITS" in rel_types
    
    conn.close()
