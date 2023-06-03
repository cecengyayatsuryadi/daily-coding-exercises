# Depth-First Search: Implement the depth-first search algorithm to traverse a graph and visit all its nodes.


def depth_first_search(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(
                graph[vertex] - visited
            )  # Add the unvisited vertices to the stack

    return visited


graph = {0: {0, 1, 3, 4, 2}, 1: {1, 3, 4, 2}, 2: {2}, 3: {3, 4, 2}, 4: {4, 2}}

print(depth_first_search(graph, 0))
