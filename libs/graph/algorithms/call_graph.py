from typing import Dict, List, Set, Tuple
from .bfs import bfs_traverse

def get_call_graph_reachable(
    start_function: str,
    get_calls: dict,
    reverse: bool = False
) -> List[str]:
    """
    Finds either all transitively called functions (reverse=False)
    or all transitive callers of start_function (reverse=True).
    """
    def neighbors_fn(func: str) -> List[str]:
        return get_calls.get(func, [])

    return bfs_traverse(start_function, neighbors_fn)
