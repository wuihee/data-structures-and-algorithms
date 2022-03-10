"""
Optimal Merge Pattern

Given n number of sorted files, the optimal merge pattern merges the files
in the least amount of computational time possible.
"""

import heapq


def optimal_merge(files):
    """
    Find the minimum merging cost of merging a list of sorted files.

    Parameters
    ----------
    files : Array of sorted files, where files[i] is the size of the ith file.
    """

    # Initialize min-heap from files.
    cost = 0
    heapq.heapify(files)

    # Greedy Choice: Merge the smallest two files and add the merged file
    # back into the heap. Keep going until there is one file left.
    while len(files) > 1:
        merged = heapq.heappop(files) + heapq.heappop(files)
        cost += merged
        heapq.heappush(files, merged)

    # Return minimum merging cost.
    return cost
    