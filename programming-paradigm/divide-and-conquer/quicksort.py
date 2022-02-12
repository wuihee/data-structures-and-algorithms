"""
Sort an unsorted list via basic quicksort.
"""

import random


def quicksort(array, low, high):
    """
    Sort array in-place using the quicksort algorithm.

    Parameters
    ----------
    array : Unsorted array.
    low : Lowest bound of array to be sorted.
    high : Highest bound of array to be sorted.
    """

    # low < high means there is still work left to do.
    if low < high:
        # Random pivot.
        i = random.randrange(low, high)
        array[high], array[i] = array[i], array[high]

        # Partition the array and find the position of the pivot.
        pivot_pos = partition(array, low, high)
        # Recursively solve for sub-arrays to the left and right of the pivot.
        quicksort(array, low, pivot_pos - 1)
        quicksort(array, pivot_pos + 1, high)


def partition(array, low, high):
    """
    Partition the array and return a pivot position.

    Parameters
    ----------
    array : Unsorted array.
    low : Lowest bound of array to be sorted.
    high : Highest bound of array to be sorted.
    """

    # Let the pivot element be the last element in the sub-array.
    pivot = array[high]
    # Let i be the index position which separates elements less than and
    # greater than the pivot.
    i = low - 1

    for j in range(low, high):
        # i will always point to an element <= than pivot.
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap the pivot with i + 1 and return the pivot's new position.
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def stress_test():
    for i in range(1000):
        array = random.sample(range(0, 20), 7)
        quicksort_ans = array
        quicksort(quicksort_ans, 0, len(array) - 1)
        correct_ans = sorted(array)

        if quicksort_ans != correct_ans:
            print('Wrong')
            print(f'array: {array}')
            print(f'correct answer: {correct_ans}')
            print(f'quicksort: {quicksort_ans}')
            break
        print('Correct')


stress_test()
