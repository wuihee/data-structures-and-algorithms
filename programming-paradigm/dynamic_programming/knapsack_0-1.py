"""
0-1 Knapsack
"""


def knapsack(W, items):
    """
    Bottom-up dynamic programming solution.

    Parameters
    ----------
    W : Capacity of knapsack.
    items : Each item contains (weight, value).
    """

    n = len(items)
    dp = [[0 for _ in range(W + 1)] * (n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            
            # Option 1: don't include ith item.
            dp[i][w] = dp[i - 1][w]

            # Option 2: include ith item.
            if items[i].weight <= w:
                value = dp[w - items[i].weight][i - 1] + items[i].value
                if dp[i][w] < value:
                    dp[i][w] = value

    return dp[n][W]
