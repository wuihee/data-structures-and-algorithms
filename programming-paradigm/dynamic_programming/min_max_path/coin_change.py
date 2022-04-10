"""
Coin Change

Given a sum of money and a list of coin demoniations available, find the
minimum number of coins that can be used to change the sum of money.
"""


def coin_change_naive(coins, amount):
    """
    Naive solution that uses backtracking.

    Parameters
    ----------
    coins : Coin denominations available.
    amount : Amount of money to change.
    """

    # Base case: nothing left to change.
    if amount == 0:
        return 0

    # Minimum amount of coins to change.
    min_change = float('inf')

    # Recursively try all possibilities.
    for c in coins:
        change = -1

        # Determine if current denomination is valid for amount remaining.
        if amount >= c:
            change = coin_change_naive(coins, amount - c)

        # If variable change was updated, update min_change.
        if change != -1:
            min_change = min(min_change, change + 1)

    # If min_change was not updated, there is no valid solution.
    # Otherwise, return min_change.
    return -1 if min_change == float('inf') else min_change


def coin_change(coins, amount):
    """
    Bottom-up solution which uses dynamic programming.
    """

    # Initialize dynamic programming table.
    # T[i] represents the minimum change for amount == i.
    T = [float('inf') for _ in range(amount + 1)]

    # Fill up DP table bottom-up.
    for i in range(amount + 1):

        # Base case: when amount == 0, min change is 0.
        if i == 0:
            T[i] = 0

        # Try all possible denominations and select the one with gives the min.
        # change.
        for c in coins:
            if i >= c:
                T[i] = min(T[i], T[i - c] + 1)

    return -1 if T[amount] == float('inf') else T[amount]


def coin_change_rec(coins, amount, T={0: 0}):
    """
    Recursive dynamic programming solution.

    Parameters
    ----------
    coins : Coin denominations available.
    amount : Amount of money to change.
    T : Dyanmic programming table.
    """

    # Check if solution was already calculated.
    if T[amount]:
        return T[amount]

    for c in coins:
        if amount >= c:
            change = coin_change_rec(coins, amount - c, T)
            if change != -1:
                change += 1
            T[amount] = change

    return -1 if not T[amount] else T[amount]


coins = [1, 3, 5]
amount = 10
print(coin_change_naive(coins, amount))
