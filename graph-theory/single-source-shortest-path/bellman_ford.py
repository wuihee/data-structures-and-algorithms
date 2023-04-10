"""
Bellman-Ford Algorithm for Single-Source Shortest Path.

Used to find the SSSP in a graph where edge values may be negative or contain
negative cycles.

1. Relax all edges. Repeat V - 1 times, where V is the number of vertices in
   the graph.
2. This works because at minimum, the shortest path from the source to its
   immediate neighbor will be found through relaxation. And carrying forward,
   the shortest path from the neighbor to the next node will be found and
   so forth.
3. Once done, relax edges one more time and if there are any changes, it means
   a negative cycle is found.

Time Complexity: O(V^2 + VE)
"""


def bellman_ford(V: int, edges: list[tuple[int]], source: int) -> list[int]:
    """
    Return the shortest path from source to all other nodes.

    Args:
        V (int): The number of vertices in the graph.
        graph (list[tuple[int]]): A list of all edges in the graph, where
                                  edges[i] -> (node, neighbor, weight).
        source (int): The source of the graph.

    Returns:
        list[int]: Returns a list of distances indicating the shortest path
                   from source to the ith node.
    """

    distances = [float('inf')] * V
    distances[source] = 0

    # Relaxation.
    for _ in range(V - 1):
        for node, neighbor, weight in edges:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = distances[node] + weight

    # Check for negative cycles.
    for _ in range(V - 1):
        for node, neigbor, weight in edges:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = float('inf')

    return distances
