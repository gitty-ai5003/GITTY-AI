from typing import Dict, List, Set
from .bfs import bfs_traverse

def get_dependency_chain(
    target_package: str,
    get_package_dependencies: dict
) -> List[str]:
    """
    Returns the downstream dependency chain (everything that depends on target_package).
    """
    def neighbors_fn(pkg: str) -> List[str]:
        return get_package_dependencies.get(pkg, [])

    return bfs_traverse(target_package, neighbors_fn)
