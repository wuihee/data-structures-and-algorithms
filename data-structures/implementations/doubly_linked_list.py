class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def clear(self):
        """Clear data in list."""
        # Initialize traversal node object.
        trav = self.head

        # Traverse list and clear all nodes.
        while trav is not None:
            next = trav.next
            trav.prev = trav.next = trav.data = None
            trav = next

        self.head = self.tail = trav = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_last(self, elem):
        """Add elem to the end of linked list."""
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.tail.next = Node(elem, None, self.tail)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, elem):
        """Add elem to the start of linked list."""
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.head.prev = Node(elem, self.head, None)
            self.head = self.head.prev
        self.size += 1

    def add_at(self, elem, idx):
        """Add elem at index idx."""
        if idx < 0 or idx > self.size:
            raise IndexError('you exceeded the range bitch.')

        if idx == 0:
            self.add_first(elem)

        elif idx == self.size:
            self.add_last(elem)

        else:
            temp = self.head
            # idx - 1 because temps is already at head.
            for _ in range(idx - 1):
                temp = temp.next
            new_node = Node(elem, temp.next, temp)
            temp.next.prev = new_node
            temp.next = new_node
            self.size += 1

    def peek_first(self):
        if self.is_empty():
            raise IndexError('List is empty dumbass.')
        return self.head

    def peek_last(self):
        if self.is_empty():
            raise IndexError('List is empty dumbass')
        return self.tail

    def pop_first(self):
        """Pop the first element of the linked list."""
        if self.is_empty():
            raise IndexError('No first element you dipshit.')
        else:
            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return data

    def pop_last(self):
        """Pop the last element of the linked list."""
        if self.is_empty():
            raise IndexError('LIST IS EMPTY GODDAMNIT.')
        else:
            data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return data

    def pop(self, node):
        """Pops arbitrary node from linked list."""
        # Use pop_first() or pop_last() if node is at the head or tail.
        if node.prev is None:
            return self.pop_first()
        elif node.next is None:
            return self.pop_last()

        # Make pointers of adjacent nodes skip over 'node'.
        node.prev.next = node.next
        node.next.prev = node.prev

        # Temporarily store data.
        data = node.data

        # Memory cleanup.
        node = None

        # Reduce size of linked-list.
        self.size -= 1

        return data

    def pop_at(self, idx):
        """Pop node at idx."""
        # Check if idx is within range of list.
        if idx < 0 or idx >= self.size:
            raise IndexError('Index given out of range.')

        # Traverse the list until idx, then pop that node.
        trav = self.head
        for i in range(self.size):
            if i == idx:
                return self.pop(trav)
            trav = trav.next

    def pop_value(self, value):
        """Remove node of data=value."""
        # Create traversal node object.
        trav = self.head

        # Search for and remove value in list.
        for _ in range(self.size):
            if trav.data == value:
                self.pop(trav)
                return True

        return False

    def index_of(self, value):
        """Return the index of 'value'."""
        # Initialize traversal node object.
        trav = self.head

        # Search list for 'node'.
        for i in range(self.size):
            if trav.data == value:
                return i
            trav = trav.next

        # If not found, return -1
        return -1

    def contains(self, node):
        """Returns if list contains 'node'."""
        return self.index_of(node) != -1

    def to_string(self):
        # Initialize traversal node object.
        trav = self.head

        # Empty string to store values.
        string = ''

        # Loop through list and add node values to 'string'.
        for _ in range(self.size):
            string += str(trav.data)
            trav = trav.next

        return string
