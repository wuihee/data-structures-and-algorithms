"""
279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum
to n.
"""


def num_squares_naive(n, squares):
    """
    Naive recursive solution.
    
    Paramters
    ---------
    n : The input integer.
    squares : List of square numbers <= n.
    """

    if n == 0:
        return 0

    min_squares = float('inf')

    for s in squares:
        if s <= n:
            n_squares = num_squares_naive(n - s, squares) + 1
            min_squares = min(min_squares, n_squares)

    return min_squares


def num_squares_rec(n, squares, dp):
    """Memoized recursive solution."""

    if n == 0:
        dp[0] = 0
        return 0

    min_squares = float('inf')

    for s in squares:
        if s <= n:
            if dp[n - s] != -1:
                n_squares = dp[n - s] + 1
            else:
                n_squares = num_squares_rec(n - s, squares, dp) + 1
            min_squares = min(min_squares, n_squares)
            dp[n] = min_squares

    return dp[n]


def num_squares(n):
    """
    Bottom-up dynamic programming solution.
    """

    dp = [0] + [float('inf')] * n

    for i in range(1, n + 1):
        dp[i] = min(dp[i - j ** 2] for j in range(1, int(i ** 0.5) + 1)) + 1

    return dp[n]
