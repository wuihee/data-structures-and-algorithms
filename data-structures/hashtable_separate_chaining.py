class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        """
        Initialize hash table.

        Parameters
        ----------
        capacity : Default capacity of the hash table.
        size : Number of elements current in the hash table.
        buckets : The array which elements are stored in.
        """
        self.capacity = 30
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash_func(self, key):
        """Given a key, hash it and return an index."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Given a key-value pair into the hash table."""
        self.size += 1
        idx = self.hash_func(key)
        node = self.buckets[idx]
        # If the chain is empty, inset straight away.
        if not node:
            self.buckets[idx] = Node(key, value)
            return None
        # Otherwise, insert at the end of the chain.
        else:
            while node.next:
                # If same key already exists, update it's value.
                if node.key == key:
                    node.value = value
                    break
                node = node.next
            node.next = Node(key, value)

    def find(self, key):
        idx = self.hash_func(key)
        node = self.buckets[idx]
        while node and node.key != key:
            node = node.next
        if not node:
            return None
        else:
            return node.value

    def remove(self, key):
        idx = self.hash_func(key)
        node = self.buckets[idx]
        prev = None
        while node and node.key != key:
            prev = node
            node = node.next

        # Node to delete wasn't found.    
        if not node:
            return None
        else:
            self.size -= 1
            result = node.value
            # If node to delete is the first node in the chain,
            if not prev:
                self.buckets[idx] = node.next
                node.next = None
            else:
                prev.next = prev.next.next
            return result


hash_table = HashTable()
hash_table.insert('a', 1)
hash_table.insert('b', 2)
