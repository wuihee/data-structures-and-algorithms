"""
Recursive binary search algorithm via divide and conquer.
"""


def binary_search(array, key, low, high):
    """
    Return position of key in array if found, else -1.

    Parameters
    ----------
    array : Sorted array to be searched.
    key : Element to search for.
    high: Upper-bound index position of the current search.
    low: Lower-bound index position of the current search.
    """

    # Base case: element not found.
    if high < low:
        return -1

    mid = low + (high - low) // 2
    # If key is less than array[mid], search left half of array.
    if key < array[mid]:
        return binary_search(array, key, low, mid - 1)
    # If key is more than array[mid], search right half of array.
    elif key > array[mid]:
        return binary_search(array, key, mid + 1, high)
    # Otherwise, key is equal to array[mid]. Return position of key.
    else:
        return mid


array = [2, 3, 4, 10, 40]
x = 10
print(binary_search(array, x, 0, len(array) - 1))
