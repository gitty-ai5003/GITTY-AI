from typing import Dict, List, Set, Callable, Any

def bfs_traverse(
    start_node: str,
    get_neighbors: Callable[[str], List[str]],
    visit_fn: Callable[[str], None] = None
) -> List[str]:
    visited: Set[str] = {start_node}
    queue: List[str] = [start_node]
    traversal_order: List[str] = []

    while queue:
        current = queue.pop(0)
        traversal_order.append(current)
        if visit_fn:
            visit_fn(current)
            
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order
