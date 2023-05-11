"""
Longest Increasing Subsequence
"""


from functools import cache


def LIS_naive(A) -> int:
    """
    Recursively find the longest increasing subsequence in given array.

    Parameters
    ----------
    A : Array of integers.
    """

    @cache
    def aux(i) -> int:
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


def lis_iterative(A: list[int]) -> int:
    """
    Find the longest increasing subsequence of an integer array.

    Args:
        A (list[int]): Integer array.

    Returns:
        int: Length of LIS.
    """
    n = len(A)

    # Let dp[i] be the LIS from A[:i + 1].
    # dp[i] = dp[j] + 1 if A[j] < A[i].
    dp = [0] * n
    dp[0] = 1

    # Check all previous LIS and find the longest one.
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[n - 1]


A = [3, 10, 2, 11]
print(LIS_naive(A))
