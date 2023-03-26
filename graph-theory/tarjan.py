"""
Tarjan's Algorithm for finding strongly-connected components (SCC) in a graph.

The low-link value of a node is the smallest (lowest) node id reachable from 
that node (including itself) when doing a DFS.

We should be able to find the SCC of the graph buy grouping together similar
low-link values.

However, the low-link values can change depending on the order of which nodes
are visited in the DFS.

Therefore, Tarjan's algorithm uses a stack containing a list of valid nodes
from which low-link values come from.

Nodes are added to the stack when they're explored for the first time, and are 
removed each time a complete SCC is found.
"""


class Graph:
    def __init__(self, n: int, graph: list[list[int]]) -> None:
        """
        Tarjan's strongly connected components algorithm.

        Args:
            n (int): Number of nodes in the graph.
            graph (list[list[int]]): Adjacency list of nodes.
        """

        # Initialize attributes.
        self.n = n
        self.graph = graph

        # The current node ID.
        self.node_id = 0

        # The total number of SCCs.
        self.scc_count = 0

        # node_ids[i] is the ID of the ith node.
        self.node_ids = [-1] * self.n

        # low_links[i] is the low link value of the ith node.
        self.low_links = [0] * self.n

        # on_stack[i] is whether node i is on the stack.
        self.on_stack = [False] * self.n

        # Stack used for the algroithm
        self.stack = []

    def tarjan(self) -> list[int]:
        """
        Executes Tarjan's algorithm.

        Returns:
            list[int]: returns the list of low link values.
        """
        for i in range(self.n):
            if self.node_ids[i] == -1:
                self.dfs(i)

        return self.low_links

    def dfs(self, at: int) -> None:
        """
        Perform DFS starting from node 'at' and update low link values.

        Args:
            at (int): the current node.
        """

        # Append current node to stack.
        self.stack.append(at)

        # Set current node to be on stack.
        self.on_stack[at] = True

        # Set the node id and the low link value of the current node to be
        # the current node id.
        self.node_ids[at] = self.low_links[at] = self.node_id

        # Increment current node id.
        self.node_id += 1

        # DFS all unvisited nodes.
        for neighbor in self.graph[at]:
            if self.node_ids[neighbor] == -1:
                self.dfs(neighbor)

            # On the callback, if neighbor is on the stack, update its low link
            # value.
            if self.on_stack[neighbor]:
                self.low_links[at] = min(self.low_links[at], self.low_links[neighbor])

        # Once we've found a SCC i.e. a cycle
        if self.node_ids[at] == self.low_links[at]:

            # Pop all nodes from the stack.
            while self.stack:
                node = self.stack.pop()

                # Update on_stack.
                self.on_stack[node] = False

                # Update the low link value of the nodes in the SCC.
                self.low_links[node] = self.node_ids[at]

                # Exit out of the SCC.
                if node == at:
                    break

            # Increase the number of SCCs we've found by 1.
            self.scc_count += 1
