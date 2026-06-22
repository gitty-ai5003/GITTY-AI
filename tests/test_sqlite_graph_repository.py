import pytest
import os
from services.graph_service.infrastructure.repositories.sqlite_graph_repository import SQLiteGraphRepository

def test_sqlite_graph_repository_crud_and_traversals(tmp_path):
    db_path = str(tmp_path / "test_gitty_graph.db")
    repo = SQLiteGraphRepository(db_path=db_path)

    # 1. Repository metadata operations
    repo.save_repository("r1", "test-repo", "/home/test", "python", "2026-06-22T00:00:00Z", "abc123hash")
    db_repo = repo.get_repository("r1")
    assert db_repo is not None
    assert db_repo["name"] == "test-repo"
    assert db_repo["hash"] == "abc123hash"
    
    assert repo.get_repository("non_existent_repo") is None

    # 2. Node operations
    repo.add_node("n1", "Class", {"name": "UserClass", "path": "user.py", "custom_prop": 42})
    repo.add_node("n2", "Function", {"name": "get_user", "path": "user.py", "return_type": "str"})
    repo.add_node("n3", "Call", {"name": "hash_password", "path": "user.py"})

    node = repo.get_node("n1")
    assert node is not None
    assert node["name"] == "UserClass"
    assert node["custom_prop"] == 42
    assert node["type"] == "Class"

    assert repo.get_node("non_existent_node") is None

    # 3. Edge operations
    repo.add_edge("n1", "n2", "CONTAINS", {"weight": 1.0})
    repo.add_edge("n2", "n3", "CALLS", {})
    
    outbound = repo.get_outbound_edges("n1")
    assert len(outbound) == 1
    assert outbound[0]["target_node"] == "n2"
    assert outbound[0]["relationship_type"] == "CONTAINS"

    # 4. Traversal BFS & DFS
    # Direct traversal
    bfs_order = repo.traverse_bfs("n1", edge_types=[])
    assert bfs_order == ["n1", "n2", "n3"]

    dfs_order = repo.traverse_dfs("n1", edge_types=[])
    assert dfs_order == ["n1", "n2", "n3"]

    # Traversal with edge types filter
    bfs_filtered = repo.traverse_bfs("n1", edge_types=["CONTAINS"])
    assert bfs_filtered == ["n1", "n2"]

    dfs_filtered = repo.traverse_dfs("n1", edge_types=["CONTAINS"])
    assert dfs_filtered == ["n1", "n2"]

    # 5. Shortest path finder
    path = repo.get_shortest_path("n1", "n3")
    assert path == ["n1", "n2", "n3"]
    
    # Path to self
    assert repo.get_shortest_path("n1", "n1") == ["n1"]
    
    # Unreachable path
    repo.add_node("n4", "Class", {"name": "Isolated", "path": "isolated.py"})
    assert repo.get_shortest_path("n1", "n4") == []

    # 6. Schema summary
    summary = repo.get_schema_summary()
    assert summary["repositories_count"] == 1
    assert summary["nodes_count"] == 4
    assert summary["edges_count"] == 2

    # 7. Remove edge and node
    repo.remove_edge("n2", "n3", "CALLS")
    assert repo.get_shortest_path("n1", "n3") == []

    repo.remove_node("n1")
    assert repo.get_node("n1") is None

    # 8. Clear database
    repo.clear_database()
    summary_empty = repo.get_schema_summary()
    assert summary_empty["repositories_count"] == 0
    assert summary_empty["nodes_count"] == 0
    assert summary_empty["edges_count"] == 0
