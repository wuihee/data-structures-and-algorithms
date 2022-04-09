"""
Leetcode Problem No. 120

Given an integer array traingle, find the minimum path sum from the top to the
bottom. If you are on index i in the first row, you can move to index i or
i + 1 on the next row.
"""


def min_total_naive(triangle, row, col):
    """
    Naive recursive solution.

    Parameters
    ----------
    triangle : Input array.
    row : Current row coordinate.
    col : Current column coordinate.
    """

    # Base case: If current position is the last row, simply return the value
    # of the current cell.
    if row == len(triangle) - 1:
        return triangle[row][col]

    # Only test for i + 1 in the next row if the current position is at most at
    # the edge of the current row.
    if col <= len(triangle[row]):
        sum_1 = min_total_naive(triangle, row + 1, col + 1)
    else:
        sum_1 = float('inf')
    sum_2 = min_total_naive(triangle, row + 1, col)

    return min(sum_1, sum_2) + triangle[row][col]


def min_total(triangle):
    """
    Bottom-up dynamic programming solution.

    Parameters
    ----------
    triangle: Input array.
    """
    
    # Initialize the dynamic programming table; it has the same structure as
    # the triangle array. T[row][col] represents the optimal solution for
    # triangle at row, col.
    n = len(triangle)
    T = [[float('inf') for _ in range(i)] for i in range(1, n + 1)]

    # Fill in the dynamic programming table from the back - bottom-up.
    for row in range(n - 1, -1, -1):
        for col in range(len(triangle[row])):

            # Base case: at the bottom row, the minimum sum will simply be the
            # current cell of the triangle array.
            if row == n - 1:
                T[row][col] = triangle[row][col]

            # Otherwise, find the minimum sum from the two options.
            else:
                T[row][col] = min(T[row + 1][col], T[row + 1][col + 1])
                T[row][col] += triangle[row][col]

    return T[0][0]


def min_total_rec(triangle, row, col, T):
    """
    Top-down recursive dynamic programming solution.

    Parameters
    ----------
    triangle : Input array.
    row : Current row coordinate.
    col : Current column coordinate.
    T : Dynamic programming table.
    """

    # Base case: return value of current cell in triangle if current position
    # is at the bottom row.
    if row == len(triangle) - 1:
        T[row][col] = triangle[row][col]

    # Check if solution is already found in dynamic programming table and
    # return it if it is.
    if T[row][col] != float('inf'):
        return T[row][col]

    # Otherwise, recursively calculate the minimum sum for the current
    # position.
    sum_1 = min_total_rec(triangle, row + 1, col, T)
    if col <= len(triangle[row]):
        sum_2 = min_total_rec(triangle, row + 1, col + 1, T)
    else:
        sum_2 = float('inf')
    
    # Update the dynamic programming table and return the solution.
    T[row][col] = min(sum_1, sum_2) + triangle[row][col]
    return T[row][col]
