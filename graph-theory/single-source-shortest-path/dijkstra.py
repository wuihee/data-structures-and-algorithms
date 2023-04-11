"""
Dijkstra's Single-Source Shortest Path Algorithm

Used to find the SSSP in a graph with no negative edge weights and cycles.
It has a time complexity better than Bellman-Ford.

1. Initialize a distance array, where distance[i] is the shortest path from the
   source node to node i.
2. Push the (distance from source node, node) onto a priority queue.
3. Pop the next node off the priority queue, and for each of its neighbors,
   perform relaxation for distance[neighbor].
4. Afterwards enqueue (edge weight, neighbor) on the priority queue.
5. Greedy Choice: The priority queue will always choose the next neighbor with
   the least weight.


Time Complexity: O(V^2)

"""

import heapq


def dijkstra(V: int, graph: list[list[tuple[int]]], source: int) -> list[int]:

    """
    Return the SSSP from the source.

    Args:
        V (int): Number of vertices / nodes in the graph.
        graph (list[list[tuple[int]]]): Adjacency list of graph, where

                                        graph[node] -> (neighbor, weight)
        source (int): Starting node.

    Returns:
        list[int]: Returns array distance, where distance[i] is the shortest
                   path from source to node i.

    """

    distance = [float('inf')] * V
    distance[source] = 0

    # Initialize priority queue
    pq = [(0, source)]

    while pq:

        # Greedy choice by nature of priority queue.
        current_distance, node = heapq.heappop(pq)

        if current_distance > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            next_distance = current_distance + weight

            # Relaxation.
            if next_distance < distance[neighbor]:
                distance[neighbor] = next_distance
                heapq.heappush(pq, (next_distance, neighbor))

    return distance
