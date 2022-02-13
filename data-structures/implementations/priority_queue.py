class PriorityQueue:
    def __init__(self, array=[]):
        """Max-Heap"""
        self.heap = array
        self.build_heap(self.heap)

    def parent(self, i):
        """Return the parent of node i."""
        return (i - 1) // 2

    def left_child(self, i):
        """Return the left child of node i."""
        left = 2 * i + 1
        return left if left < len(self.heap) else i

    def right_child(self, i):
        """Return the right child of node i."""
        right = 2 * i + 2
        return right if right < len(self.heap) else i

    def build_heap(self, array):
        n = len(array)
        for i in range(n // 2, -1, -1):
            self.sift_down(i)

    def sift_up(self, i):
        # While i is not root and i's value is greater than it's parent's,
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            # Swap self and parent.
            parent = self.parent(i)
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            # Move up.
            i = parent

    def sift_down(self, i):
        # Check if either right or left child is greater than i.
        max_idx = i
        left = self.left_child(i)
        right = self.right_child(i)

        if self.heap[left] > self.heap[max_idx]:
            max_idx = left
        if self.heap[right] > self.heap[max_idx]:
            max_idx = right

        # Swap i with greater child.
        if i != max_idx:
            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            self.sift_down(max_idx)

    def insert(self, val):
        """Insert val into priority queue."""
        self.heap.append(val)
        # Sift the last element up.
        self.sift_up(len(self.heap) - 1)

    def pop(self):
        """Pop element with the most priority, i.e. root."""
        root = self.heap[0]
        # Replace root with the last node.
        self.heap[0] = self.heap[-1]
        # Remove the last element.
        self.heap.pop()
        # Heap may have had the last element popped out.
        if self.heap:
            self.sift_down(0)
        return root

    def remove(self, i):
        """Remove node i."""
        self.heap[i] = float('inf')
        self.sift_up(i)
        self.pop()

    def change_priority(self, i, val):
        """Change the priority (i.e. value) of ith node."""
        old_val = self.heap[i]
        self.heap[i] = val
        if val > old_val:
            self.sift_up(i)
        else:
            self.sift_down(i)
