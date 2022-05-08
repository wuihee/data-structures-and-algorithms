"""
650. 2 Keys Keyboard

There is only one character 'A' on the screen of a notepad. You can perform one
of two operations on this notepad for each step:
    1. Copy All: You can copy all the characters present on the screen.
    2. Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the
character 'A' exactly n times on the screen.
"""


def min_steps_naive(n):
    """Naive recursive solution."""

    # Base case: you start off with 1 'A' already on the screen, therefore, the
    # number of operations needed to get to 1 'A' is 0.
    if n == 1:
        return 0

    min_ops = float('inf')
    for i in range(1, n):
        if n % i == 0:
            ops = min_steps_naive(i) + n // i
            min_ops = min(min_ops, ops)

    return min_ops


def min_steps_rec(n, dp):
    """Memoized dynamic programming solution."""
    if n == 1:
        return 0

    # Check if solution was already computed in dp table.
    if dp[n] != float('inf'):
        return dp[n]

    for i in range(1, n):
        if n % i == 0:
            ops = min_steps_rec(i, dp) + n // i
            dp[n] = min(dp[n], ops)

    return dp[n]


def min_steps(n):
    """Bottom-up dynamic programming solution."""

    # dp[i] represents the min. no. of operations needed to get to i "A"s.
    dp = [float('inf') for _ in range(n + 1)]
    
    # Base case
    dp[1] = 0

    # Calculate dp[i] from 2 <= i <= n
    for i in range(2, n + 1):

        # If n % i != 0, there is no point in calculating dp[i].
        if n % i == 0:

            # Then try every possibility from 1 to i
            for j in range(1, i):
                if i % j == 0:
                    ops = dp[j] + i // j
                    dp[i] = min(dp[i], ops)

    return dp[n]
