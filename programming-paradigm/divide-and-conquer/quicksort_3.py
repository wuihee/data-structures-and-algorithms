"""
Sort an unsorted list via 3 way partition quicksort.
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

        p, q = partition(array, low, high)
        quicksort(array, low, p - 1)
        quicksort(array, q + 1, high)


def partition(array, low, high):
    """
    Partition the array and return a pivot position.

    Parameters
    ----------
    array : Unsorted array.
    low : Lowest bound of array to be sorted.
    high : Highest bound of array to be sorted.
    """

    pivot = array[high]
    # array[low ... start] contain elements < pivot.
    # array[start ... i] contain elements == pivot.
    start = i = low
    # array[i ... end] contain unknown elements.
    # array[end ... high] contain elements > pivot.
    end = high - 1

    while i <= end:
        if array[i] < pivot:
            array[start], array[i] = array[i], array[start]
            start += 1
            i += 1
        elif array[i] == pivot:
            i += 1
        else:
            array[i], array[end] = array[end], array[i]
            end -= 1

    array[high], array[i] = array[i], array[high]
    return start, i


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
