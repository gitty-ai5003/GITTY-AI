from typing import Dict, List, Set, Callable, Any

def dfs_traverse(
    start_node: str,
    get_neighbors: Callable[[str], List[str]],
    visit_fn: Callable[[str], None] = None
) -> List[str]:
    visited: Set[str] = set()
    traversal_order: List[str] = []

    def _dfs(node: str):
        visited.add(node)
        traversal_order.append(node)
        if visit_fn:
            visit_fn(node)
            
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start_node)
    return traversal_order
