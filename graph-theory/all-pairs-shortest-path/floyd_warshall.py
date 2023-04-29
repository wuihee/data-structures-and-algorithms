"""
Floyd Warshall Algorithm.

Floyd Warshall is an all-pairs shortest paths (APSP) algorithm.
Given a graph, find the shortest path between i, j for all nodes i, j.
"""


def floyd_warshall(n, pairs) -> tuple[list, list]:
    """
    Find the APSP between all nodes.

    Args:
        n (int): Number of nodes in the graph from 1, ..., n.
        pairs (list[list[int]]): pairs[i] = [a, b, w], which represents that
                                 node a is connected node b with a weight of w.

    Returns:
        tuple[list, list]: Returns graph of APSP, and path which reconstructs
                           the shortest path of each node.
    """

    # Initialize adjacency matrix.
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for a, b, w in pairs:
        graph[a][b] = w

    # Initialize matrix for path reconstruction.
    # path[i][j] is the next node from node i in the path from i to j.
    path = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):

            # First check if there exists a path from i to j.
            if graph[i][j] != float('inf'):
                path[i][j] = j

    # Reminder: 1, n + 1 because our nodes are numbered from 1 to n.
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] + graph[k][j] < graph[i][j]:

                    # FW Recurrence Relation / Relaxation
                    graph[i][j] = graph[i][k] + graph[i][j]

                    # In the shortest path from node i to j, we need
                    # to first go to node k. Thus, the next node after
                    # node i is the next node in the path from node i
                    # to node k.
                    path[i][j] = path[i][k]

    graph, path = find_negative_cycles(graph, path)
    return graph, path


def find_negative_cycles(graph, path):
    """
    Test for negative cycles in the graph.
    """

    n = len(graph)

    # Run FW algorithm again and if the values can be improved neagtive
    # cycles exist.
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):

                # If a negative cycle exists, set relevant node to -inf.
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = -float('inf')

                    # Since there's a negative cycle, update the path.
                    path[i][j] = -1

    return graph, path


def reconstruct_path(graph, path, start, end):
    """
    Reconstruct the shortest path between 2 nodes.

    Parameters
    ----------
    graph - adjacency matrix denoting shortest APSP.
    path - path[i][j] indicates the next node after i in the path
           from node i to j.
    start - start node.
    end - end node.
    """

    current_path = []

    # Check if there exists a path between the start and end node.
    if graph[start][end] == float('inf'):
        return current_path

    # Track current node.
    at = start
    while at != end:

        # Negative cycle
        if at == -1:
            return None

        current_path.append(at)
        at = current_path[at][end]

    # Finally, check if the last node has a negative cycle within
    # itself.
    if current_path[at][end] == -1:
        return None

    current_path.append(end)
    return current_path
