class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x) -> int:
        """Return the ID/root of element x."""
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> None:
        """Merge elements x and y."""
        x_root = self.find(x)
        y_root = self.find(y)

        # Return nothing if x and y are already grouped.
        if x_root == y_root:
            return

        # Hang y on x if x's tree is greater than y's.
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root

        # Else, hang x on y.
        else:
            self.parent[x_root] = y_root
            # If both trees are the same height,
            # increase the rank (i.e. height) of y by 1.
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] += 1
