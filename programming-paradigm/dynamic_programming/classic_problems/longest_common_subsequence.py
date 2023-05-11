"""
Longest Common Subsequence

Given two integer arrays, find the longest common subsequence.
"""

array_1 = []
array_2 = []


def lcs_recursive(i: int, j: int) -> int:
    """
    Returns the LCS of array_1[i:] and array_2[j:]

    Args:
        i (int): Front index of the first array.
        j (int): Front index of the ssecond array.

    Returns:
        int: Length of the LCS.
    """

    # Base case: reached the end of either array.
    if i == len(array_1) or j == len(array_2):
        return 0

    # Optimal substructure: if current elements are the same, remove them
    # (i.e. add them to the LCS) and reduce the subproblem.
    if array_1[i] == array_2[j]:
        return lcs_recursive(i + 1, j + 1) + 1

    # Otherwise, try the two options available:
    # 1. Moving forward in array_1.
    # 2. Moving forward in array_2.
    return max(lcs_recursive(i + 1, j), lcs_recursive(i, j + 1))


def lcs_iterative(array_1: list[int], array_2: list[int]) -> int:
    """
    Returns the LCS of array_1 and array_2, done so iteratively.

    Args:
        array_1 (list[int]): First integer array.
        array_2 (list[int]): Second integer array.

    Returns:
        int: Length of the LCS.
    """
    m = len(array_1)
    n = len(array_2)

    # Let dp[i][j] be the LCS of array_1[i:] and array_2[j:].
    # dp[i][j] = dp[i - 1][j - 1] + 1 if array_1[i] == array_2[j].
    # Else, dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]).
    # The reason why range(n + 1) and range(m + 1) is so that we can avoid
    # manually filling out the base case.
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if array_1[i] == array_2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
