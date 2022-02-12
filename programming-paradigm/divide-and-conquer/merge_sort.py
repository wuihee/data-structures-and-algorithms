"""
Sort an unsorted list via merge sort.
"""


def merge_sort(array):
    """
    Return sorted array using merge sort algorithm.

    Parameters:
    -----------
    array : Unsorted array.
    """

    n = len(array)
    # Base case: empty array or only contains one element.
    if n <= 1:
        return array

    # Recursively divide array into left and right halves.
    left_half = merge_sort(array[:n // 2])
    right_half = merge_sort(array[n // 2:])
    return merge(left_half, right_half)


def merge(left_half, right_half):
    """Given two sorted arrays, merge into a single sorted array."""

    # i will index left_half and j will index right_half.
    i = j = 0
    merged_array = []

    # Merge until at least one array reaches the end.
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_array.append(left_half[i])
            i += 1
        else:
            merged_array.append(right_half[j])
            j += 1

    # Add the remaining of the other array to merged_array.
    # Both arrays are added because we don't know which one is the remaining.
    return merged_array + left_half[i:] + right_half[j:]


print(merge_sort([9, 3, 2, 6, 2, 3, 7, 5]))
