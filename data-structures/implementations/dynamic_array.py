class DynamicArray:
    def __init__(self, array=[]):
        self.array = array
        self.length = len(array)

    def size(self):
        """Return the number of elements in the array."""
        return self.length

    def is_empty(self):
        """Return if the array is empty."""
        return False if self.length else True

    def get(self, i):
        """Return array[i]."""
        return self.array[i]

    def set(self, i, obj):
        """Set array[i] = obj."""
        self.array[i] = obj

    def clear(self):
        """Remove all data from array."""
        self.array = ['-' for _ in range(self.length)]
        self.length = 0

    def add(self, obj):
        """Add obj to the end of the array."""
        capacity = len(self.array)

        # If the array is at its' maximum capacity
        if self.length + 1 > capacity:
            new_cap = capacity * 2 if capacity > 0 else 1
            new_array = ['-' for _ in range(new_cap)]

            for i in range(len(self.array)):
                new_array[i] = self.array[i]
            self.array = new_array

        self.array[self.length] = obj
        self.length += 1

    def remove_at(self, i):
        """Remove item at index i."""
        if i > self.length or i < 0:
            return IndexError

        capacity = len(self.array)
        new_array = ['-' for _ in range(capacity)]

        for j in range(0, i):
            new_array[j] = self.array[j]
        for j in range(i + 1, capacity):
            new_array[j - 1] = self.array[j]

        self.array = new_array
        self.length -= 1

    def remove(self, obj):
        """Remove obj from array."""
        for i in range(len(self.array)):
            if self.array[i] == obj:
                self.remove_at(i)
                return True

        return False

    def index_of(self, obj):
        """Return the index of obj."""
        for i in range(len(self.array)):
            if self.array[i] == obj:
                return i

        return -1

    def contains(self, obj):
        """Returns true if array contains object."""
        return self.index_of(obj) != -1

    def to_string(self):
        string = ''
        for obj in self.array:
            if obj != '-':
                string += str(obj)

        return string
