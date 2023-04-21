"""
0-1 Knapsack

We are given N items where each item has some weight and profit associated with
it. We are also given a bag with capacity W. The target is to put the items
into the bag such that the sum of profits associated with them is the maximum
possible.

The constraint here is we can either put an item completely into the bag or
cannot put it at all, this is why the problem is called 0-1.
"""


def knapsack(W: int, items: int) -> int:
    """
    Bottom-up dynamic programming solution.

    Args:
        W (int): Capacity of knapsack.
        items (list[int]): Each item contains (weight, value).

    Returns:
        int: Returns the maximum possible value of items.
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
