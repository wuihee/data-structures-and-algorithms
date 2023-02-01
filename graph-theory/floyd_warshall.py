"""
Floyd Warshall Algorithm.

Floyd Warshall is an all-pairs shortest paths (APSP) algorithm.
Given a graph, find the shortest path between i, j for all nodes i, j.
"""


def floyd_warshall(n, pairs):
    """
    Find the APSP between all nodes.

    Parameters
    ----------
    n - Number of nodes in the graph from 1, ..., n.
    pairs - pairs[i] = [a, b, w], which represents that node a is connected
            node b with a weight of w.
    """

    # Initialize adjacency matrix.
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for a, b, w in pairs:
        graph[a][b] = w
