"""
Given a sorted array A, find a pair of elements A[i], A[j] such that
A[i] + A[j] == target.

This problem will showcase the two-pointers technique.
"""


def two_pointers(A: list, target: int) -> tuple:
    """
    Parameters
    ----------
    A - A sorted array.
    target - An integer such that is the sum of A[i] + A[j]

    Output
    ------
    Reutrn the indices i and j, where A[i] + A[j] == target.
    Algorithm will achieve this in O(n) with the two pointers technique.
    """

    i = 0
    j = len(A) - 1

    while i < j:
        current_sum = A[i] + A[j]

        # If the current sum is less than target, since A is sorted, we can
        # increment i to increase the sum.
        if current_sum < target:
            i += 1

        # If the sum is less than the target, we know that reducing j will
        # decrease the sum.
        elif current_sum > target:
            j -= 1

        # If the target is found, return indices i and j.
        else:
            return i, j
        
    # No two elements in A can sum up to target.
    return -1, -1
