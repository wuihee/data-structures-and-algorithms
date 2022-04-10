"""
Leetcode Problem No. 174

Given an m x n matrix dungeon. Start from the top left and either move down or
right. After each move, change your health by the number in the current move.
Return the minimum amont of initial health required to clear the dungeon with
greater than 0 health.
"""


def calc_min_HP_naive(dungeon, row, col):
    """
    Naive recursive solution.

    Parameters
    ----------
    dungeon : Input matrix.
    row : Current row position.
    col : Current column position.
    """

    m = len(dungeon)
    n = len(dungeon[0])

    if row == m - 1 and col == n - 1:
        return dungeon[row][col]

    path_1 = path_2 = float('inf')
    if row < m - 1:
        path_1 = calc_min_HP_naive(dungeon, row + 1, col)
    if col < n - 1:
        path_2 = calc_min_HP_naive(dungeon, row, col + 1)

    min_path = min(path_1, path_2) + dungeon[row][col]
    return 1 - min_path
