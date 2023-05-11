"""
Insertion Sort

Given an unsorted array, sort the array by taking each number, looping through
the sorted numbers and inserting it in its right place.

Time Complexity: O(n^2)
"""


def insertion_sort(A: list[int]) -> list[int]:
    """
    Sort a list of numbers in-place.

    Args:
        A (list[int]): Unsorted array.

    Returns:
        list[int]: Return sorted array.
    """
    n = len(A)

    # Let A[0] be the "sorted list".
    for i in range(1, n):

        # Keep track of current number you want to insert.
        key = A[i]
        j = i - 1

        # Find the correction location to insert "key".
        while j >= 0 and A[j] > key:

            # If number is greater than "key", shift it right.
            # The numbers will "shift" into A[i], but its ok since we're
            # kepping track of A[i] in "key".
            A[j + 1] = A[j]
            j -= 1

        # Once a location is found, insert "key".
        A[j + 1] = key

    return A


print(insertion_sort([4, 3, 6, 8, 3, 5, 3, 1]))
