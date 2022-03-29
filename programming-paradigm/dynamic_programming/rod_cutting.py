"""
Rod Cutting

Given a rod of n inches, and a table of prices p, where p[i] is the price which
a rod of size i inches sells for, find the maximum revenue from cutting the rod
into smaller pieces and selling them.
"""


def rod_cutting(rod, prices):
    """
    Bottom-up tabular solution for the rod cutting problem.
    
    Parameters
    ----------
    rod : The length of the rod.
    prices : Table of prices where prices[i] is the price a rod of i inches
             sells for.
    """

    # revenue[i] is the maximum revenue for a rod of i inches.
    # revenue[0] = 0 because a rod of length 0 sells for 0.
    revenue = [0 for _ in range(rod + 1)]

    for i in range(1, rod + 1):

        # Let r be a variable to temporarily store the maximum revenue for the
        # current i
        r = -float('inf')

        # Try all combinations rods up to i inches.
        for j in range(1, i + 1):
            r = max(r, prices[j] + revenue[i - j])

    return revenue[rod]


def rod_cutting_rec(rod, prices, revenue):
    """
    Recursive solution for the rod cutting problem.

    Parameters
    ----------
    rod : The length of the rod.
    prices : Table of prices where prices[i] is the price a rod of i inches
             sells for.
    revenue : Revenue[i] is the maximum revenue for a rod of i inches.
    """

    # Base case: length of rod is less or equal to 1.
    if rod <= 1:
        return prices[rod]

    # Base case: maximum revenue for length of rod was already calculated.
    if revenue[rod]:
        return revenue[rod]

    r = -float('inf')
    for i in range(1, rod + 1):
        r = max(r, prices[i] + rod_cutting_rec(prices, revenue, rod - i))
    
    # Updates table of revenue.
    revenue[rod] = r
    return r
