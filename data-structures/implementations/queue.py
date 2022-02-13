class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    def size(self):
        return self.length

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, val):
        """Add an element to the end of the queue."""
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            node = Node(val)
            self.tail.next = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        """Remove an element from the front of the queue."""
        if not self.head:
            raise IndexError('Cannot dequeue from empty queue.')
        else:
            node = self.head
            self.head = self.head.next
            return node.val
        self.length -= 1

    def peek(self):
        """Peek at the first element from the front of the queue."""
        return self.head

    def print_queue(self):
        trav = self.head
        while trav:
            print(trav.val)
            trav = trav.next
