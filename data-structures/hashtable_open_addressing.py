"""
Hash table implementation using open addressing and quadratic probing.

Classes:

    HashTable
"""


class HashTable:
    """
    Hash table implementation using open addressing and quadratic probing.

    Methods
    -------
    normalize_index
    insert
    get
    remove
    resize_table
    """
    def __init__(self):
        """
        Initialize the hashtable.

        Parameters
        ----------
        capacity : The initial capacity of the hashtable.
        load_factor : used_buckets / capacity i.e. a fraction of the size.
        threshold : Grow hashtable once load_factor > threshold.
        used_buckets : Total no. of values being used.
        key_count : Total no. of unique keys in the hashtable.
        keys : Array to store keys.
        values : Array to store values.
        """
        self.capacity = 8
        self.load_factor = 0.45
        self.threshold = self.capacity * self.load_factor
        self.used_buckets = 0
        self.key_count = 0
        self.keys = [None for _ in range(self.capacity)]
        self.values = [None for _ in range(self.capacity)]

    def probe(self, x):
        """Probe function."""
        return (x ** 2 + x) // 2

    def normalize_index(self, key):
        """Given a key return an appropriate index."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Insert or update key-value pair into hashtable."""
        if self.used_buckets >= self.threshold:
            self.resize_table()

        idx = self.normalize_index(key)
        # Current index.
        i = idx
        # Position of last tombstone.
        j = -1
        # Probe offset.
        k = 1

        while True:
            if self.keys[i] == 'TOMBSTONE':
                if j == -1:
                    j = i

            # Key we're trying to add already exists, so update it.
            elif self.keys[i] == key:
                old_value = self.values[i]
                # If there are no tombstones,
                if j == -1:
                    self.values[i] = value
                # Otherwise, swap with last tombstone.
                else:
                    self.keys[i] = 'TOMBSTONE'
                    self.values[i] = None
                    self.keys[j] = key
                    self.values[j] = value
                # Return previous value just in case.
                return old_value

            # Else, current cell is empty and we can insert.
            elif not self.keys[i]:
                # No previously encountered deleted buckets.
                if j == -1:
                    self.used_buckets += 1
                    self.key_count += 1
                    self.keys[i] = key
                    self.values[i] = value
                # Else, insert at previously seen deleted bucket.
                else:
                    self.key_count += 1
                    self.keys[j] = key
                    self.values[j] = value
                return None

            # Else, bucket is already taken so keep on probing.
            i = self.normalize_index(idx + self.probe(k + 1))

    def get(self, key):
        """Get the value associated with the given key."""
        idx = self.normalize_index(key)
        # Current index.
        i = idx
        # Position of last tombstone.
        j = -1
        # Probe offset.
        k = 1

        while True:
            if self.keys[i] == 'TOMBSTONE':
                if j == -1:
                    j = i
            # We hit a non-null key.
            elif self.keys[i]:
                # The key we want is found.
                if self.keys[i] == key:
                    # If previously encountered a deleted cell,
                    if j != -1:
                        self.keys[j] = self.keys[i]
                        self.values[j] = self.values[i]
                        self.keys[i] = 'TOMBSTONE'
                        self.values[i] = None
                        return self.values[j]
                    return self.values[i]
            # Else, element was not found.
            else:
                return None
            # Keep probing until the function returns.
            i = self.normalize_index(idx + self.probe(k + 1))

    def remove(self, key):
        """Remove key-value pair."""
        idx = self.normalize_index(key)
        k = 1

        # Probe until we find our key or hit None.
        while True:
            if self.keys[idx] == 'TOMBSTONE':
                continue
            if not self.keys[idx]:
                return None
            if self.keys[idx] == key:
                self.key_count -= 1
                old_value = self.values[idx]
                self.keys[idx] = 'TOMBSTONE'
                self.values[idx] = None
                return old_value
            idx = self.normalize_index(idx + self.probe(k + 1))

    def resize_table(self):
        """Resize the capacity of the hash table."""
        # Update capcity and threshold.
        self.capacity *= 2
        self.threshold = self.capacity * self.load_factor
        old_keys = [None for _ in range(self.capacity)]
        old_values = [None for _ in range(self.capacity)]

        # Hash table is now empty with 2x capcity.
        self.keys, old_keys = old_keys, self.keys
        self.values, old_values = old_values, self.values

        # Reset key count and buckets used.
        self.key_count = self.used_buckets = 0

        # Insert old hashtable into new, resized one.
        for i in range(len(old_keys)):
            if old_keys[i] and old_keys[i] != 'TOMBSTONE':
                self.insert(old_keys[i], old_values[i])
            old_values[i] = None
            old_keys[i] = None


hash_table = HashTable()
hash_table.insert('a', 1)
hash_table.insert('b', 2)
hash_table.insert('c', 3)
hash_table.insert('d', 4)
hash_table.insert('e', 5)
print('End of tests.')
