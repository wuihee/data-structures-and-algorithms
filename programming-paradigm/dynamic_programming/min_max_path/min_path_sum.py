"""
Minimum Path Sum: Leetcode Problem No. 64

Given an m x n grid filled with non-negative integers, find a path from the top
left to the bottom right which minimizes the sum of the numbers.
"""


def min_path_naive(grid, row, col):
    """
    Naive recursive solution.

    Parameters
    ----------
    grid : Input grid matrix.
    row : Row which the instance is currently at.
    col : Column which the instance is currently at.
    """

    m = len(grid)
    n = len(grid[0])

    # Base case: if current position is at the final cell, simply return it's
    # value.
    if row == m - 1 and col == n - 1:
        return grid[row][col]

    # Recursively find the minimum paths from the two choices of either going
    # right or down.
    path_1 = path_2 = float('inf')
    if row < m - 1:
        path_1 = min_path_naive(grid, row + 1, col)
    if col < n - 1:
        path_2 = min_path_naive(grid, row, col + 1)
    
    return min(path_1, path_2) + grid[row][col]


def min_path(grid):
    """
    Bottom-up dynamic programming solution.

    Parameters
    ----------
    grid : Input grid matrix.
    """

    # Initialize DP table where T[r][c] represents the minimum sum used to
    # reach position r, c.
    m = len(grid)
    n = len(grid[0])
    T = [[float('inf') for _ in range(n)] for _ in range(m)]

    # Fill up the DP table.
    for r in range(m):
        for c in range(n):

            # Base case: minimum sum required to reach (0, 0) is simply the
            # value of grid[0][0] (which will be added later).
            if r == 0 and c == 0:
                T[r][c] = 0

            # If current position is the first row, the minimum sum can only
            # be found from going in a straight, horizontal direction.
            elif r == 0:
                T[r][c] = T[r][c - 1]

            # Likewise, if current position is the first column, the minimum
            # sum can only befound from going down in a straight line.
            elif c == 0:
                T[r][c] = T[r - 1][c]
            
            # Fill up the other cells.
            else:
                T[r][c] = min(T[r - 1][c], T[r][c - 1])

            # Add the value of the current cell.
            T[r][c] += grid[r][c]

    return T[m - 1][n - 1]


def min_path_rec(grid, row, col, T):
    """
    Top-down dynamic programming solution.

    Parameters
    ----------
    grid : Input grid matrix.
    row : Row which the instance is currently at.
    col : Column which the instance is currently at.
    T : Dynamic programming table.
    """

    m = len(grid)
    n = len(grid[0])

    if row == m - 1 and col == n - 1:
        return grid[row][col]
    
    if T[row][col] != float('inf'):
        return T[row][col]

    path_1 = path_2 = float('inf')
    if row < m - 1:
        path_1 = min_path_naive(grid, row + 1, col, T)
    if col < n - 1:
        path_2 = min_path_naive(grid, row, col + 1, T)

    T[row][col] = min(path_1, path_2) + grid[row][col]
    return T[row][col]
