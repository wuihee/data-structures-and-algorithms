"""
Longest Increasing Subsequence
"""


from functools import cache


def LIS_naive(A):
    """
    Recursively find the longest increasing subsequence in given array.

    Parameters
    ----------
    A : Array of integers.
    """

    @cache
    def aux(i):
        # Base case
        if i == 0:
            return 1

        longest = 1
        for j in range(i):
            if A[j] < A[i]:
                longest = max(longest, aux(j) + 1)

        return longest

    lss = 1
    for j in range(len(A)):
        lss = max(lss, aux(j))

    return lss


A = [3, 10, 2, 11]
print(LIS_naive(A))
