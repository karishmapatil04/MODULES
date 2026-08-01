def dfs(graph, start):
    """
    Performs a depth-first search on the given graph, starting at the given node.

    Args:
    graph: The graph to search.
    start: The node to start the search at.

    Returns:
    A list of the nodes visited by the search, in the order in which they were visited.
    """

    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)

    return visited
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

visited = dfs(graph, 'A')

print(visited)