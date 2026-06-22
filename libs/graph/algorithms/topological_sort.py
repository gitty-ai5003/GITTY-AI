from typing import Dict, List, Set

def topological_sort(
    nodes: List[str],
    get_dependencies: Dict[str, List[str]]
) -> List[str]:
    """
    Standard Kahn's algorithm for topological sorting.
    get_dependencies defines node -> list of dependencies (edges coming INTO the node).
    """
    # Calculate in-degree (number of dependencies)
    in_degree = {node: 0 for node in nodes}
    adj_list = {node: [] for node in nodes}

    for node in nodes:
        for dep in get_dependencies.get(node, []):
            if dep in adj_list:
                adj_list[dep].append(node)
                in_degree[node] += 1

    # Queue of nodes with no dependencies (in-degree 0)
    queue = [node for node in nodes if in_degree[node] == 0]
    sorted_order = []

    while queue:
        u = queue.pop(0)
        sorted_order.append(u)

        for v in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(sorted_order) != len(nodes):
        raise ValueError("Graph has circular dependencies (cycle detected)")

    return sorted_order
