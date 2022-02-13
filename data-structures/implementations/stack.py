class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Stack:
    def __init__(self):
        self.head = Node()
        self.length = 1

    def size(self):
        return self.length

    def is_empty(self):
        return self.size() == 0

    def push(self, obj):
        """Add node before head."""
        node = Node(obj)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.head:
            raise IndexError('Cannot pop from empty stack.')
        node = self.head
        self.head = self.head.next
        return node.val

    def print_stack(self):
        trav = self.head
        while trav.next:
            print(trav.val)
            trav = trav.next
