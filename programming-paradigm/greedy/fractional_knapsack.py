"""Fractional knapsack problem."""

from collections import namedtuple


def knapsack(weights, values, capacity):
    """
    Return the maximum value the knapsack can hold.

    Parameters
    ----------
    weights : weights[i] is the weight of the ith item.
    values : values[i] is the value of the ith item.
    capacity : The maximum weight the knapsack can hold.
    """

    # Initialize items[...(weight, value)...] and sort by value per weight.
    n = len(weights)
    Item = namedtuple('Item', ['weight', 'value'])
    items = [Item(weights[i], values[i]) for i in range(n)]
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    value_taken = 0

    # Greedy Choice: Take as much as possible of the item with the most
    # value per weight.
    for i in range(n):
        if capacity == 0:
            break
        curr_item = items[i]
        weight_taken = min(capacity, curr_item.weight)
        value_taken += weight_taken / curr_item.weight * curr_item.value
        capacity -= weight_taken

    return value_taken
