class TreeNode:
    def __init__(self, index=0, children=[]):
        self.index = index
        self.children = children


class LCAEulerTour:
    def __init__(self, root, n):
        """
        Initialize LCA Euelerian Tour solver.

        Parameters
        ----------
        root : Root node of tree.
        n : Number of nodes in the tree.
        """
        self.n = n
        self.tour_index = 0
        self.setup(root)

    def setup(self, root):
        euler_tour_size = 2 * self.n - 1
        self.nodes = [TreeNode() for _ in range(euler_tour_size)]
        self.depth = [0 for _ in range(euler_tour_size)]

        # Map node index to Eulerian tour index.
        self.last = [0 for _ in range(self.n)]

        self.dfs(root)
        # self.sparse_table = ...

    def dfs(self, node, node_depth=0):
        # Reached base case
        if not node:
            return

        self.visit(node, node_depth)
        for child in node.children:
            self.dfs(child, node_depth + 1)
            self.visit(node, node_depth)

    def visit(self, node, node_depth):
        self.nodes[self.tour_index] = node
        self.depth[self.tour_index] = node_depth
        self.last[node.index] = self.tour_index
        self.tour_index += 1

    def lca(self, index1, index2):
        left = min(self.last[index1], self.last[index2])
        right = max(self.last[index1], self.last[index2])
        i = self.sparse_table.queryIndex(left, right)
        return self.nodes[i]
