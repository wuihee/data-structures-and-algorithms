"""
Iterative binary search algorithm via divide and conquer.
"""


def binary_search(array, key):
    """
    Return position of key in array if found, else -1.

    Parameters
    ----------
    array : Sorted array to be searched.
    key : Element to search for.
    """
    low = 0
    high = len(array) - 1

    # While there's still something left to search,
    while high >= low:
        mid = low + (high - low) // 2
        # Search left half of array.
        if key < array[mid]:
            high = mid - 1
        # Search right half of array.
        elif key > array[mid]:
            low = mid + 1
        # Otherwise, array[mid] == key. Return position o fkey.
        else:
            return mid

    # Key was not found.
    return -1


array = [2, 3, 4, 10, 40]
x = 10
print(binary_search(array, x))
