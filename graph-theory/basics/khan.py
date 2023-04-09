"""
Khan's Topological Sort Algorithm

1. Find the degree of each node (i.e. the number of nodes pointing toward it).
2. Continuously remove nodes with degree of 0, like peeling a layer of an
   onion.
3. While doing so, sort the nodes in topological order.
4. Keep going until the last node is reached or a cycle is discovered.
"""

import collections


def topological_sort(graph: list[list[int]]) -> list:
    """
    Return the topological ordering of a graph. Nodes are numbered 0 to n - 1.

    Args:
        graph (list[list[int]]): Adjacency list.

    Returns:
        list: Topological order of nodes in the graph.
    """
    n = len(graph)
    degree = [0] * n

    # Establish the degree of each node.
    for node in range(n):
        for neighbor in graph[node]:
            degree[neighbor] += 1

    # Initialize a queue of nodes with no other nodes pointing towards them.
    queue = collections.deque([i for i in range(n) if degree[i] == 0])
    order = [0] * n

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:

            # Update the degree since we removed node and added it to the
            # topological ordering.
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if there was a cycle.
    if len(order) != n:
        return []
    return order
