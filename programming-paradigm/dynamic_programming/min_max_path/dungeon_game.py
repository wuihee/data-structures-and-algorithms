"""
Leetcode Problem No. 174

Given an m x n matrix dungeon. Start from the top left and either move down or
right. After each move, change your health by the number in the current move.
Return the minimum amont of initial health required to clear the dungeon with
greater than 0 health.
"""


def calc_HP_naive(dungeon, r, c):
    """
    Naive recursive solution.
    
    Each function call returns the inimum HP required to go from position
    (r, c) to the end.

    Parameters
    ----------
    dungeon : Input matrix.
    r : Current row position.
    c : Current column position.
    """

    m = len(dungeon)
    n = len(dungeon[0])

    # Base case: if position exceeds the matrix, return infinity.
    if r == m or c == n:
        return float('inf')
    
    # Base case: if position is at the end, return the minimum health required
    # to survive on that cell.
    if r == m - 1 and c == n - 1:
        return -dungeon[r][c] + 1 if dungeon[r][c] <= 0 else 1

    # Head recursion: recurse all the way to the bottom and from there work
    # back up to the solution.
    go_right = calc_HP_naive(dungeon, r, c + 1)
    go_left = calc_HP_naive(dungeon, r + 1, c)

    # Take the minimum path found so far and adjust the minimum HP required
    # to account for the current cell.
    min_HP_req = min(go_right, go_left) - dungeon[r][c]

    # If min_HP_req < 0, it means only 1 HP is required.
    return min_HP_req if min_HP_req > 0 else 1


def calc_HP_rec(dungeon, dp, r, c):
    """
    Recursive dynamic programming solution.

    Paramters
    ---------
    dungeon : Input matrix.
    dp : Dynamic programming table.
    r : Current row position.
    c : Current column position. 
    """

    n = len(dungeon)
    m = len(dungeon[0])

    # Base case: if position exceeds the matrix, return infinity.
    if r == m or c == n:
        return float('inf')

    # Base case: if position is at the end, return the minimum health required
    # to survive on that cell.
    if r == m - 1 and c == n - 1:
        return -dungeon[r][c] + 1 if dungeon[r][c] <= 0 else 1

    # If the solution is already found in the dp table, return it.
    if dp[r][c] != float('inf'):
        return dp[r][c]

    # Head recursion: recurse all the way to the bottom and from there work
    # back up to the solution.
    go_right = calc_HP_rec(dungeon, dp, r, c + 1)
    go_left = calc_HP_rec(dungeon, dp, r + 1, c)
    min_HP_req = min(go_right, go_left) - dungeon[r][c]

    # Add solution to the dp table.
    dp[r][c] = 1 if min_HP_req <= 0 else min_HP_req
    return dp[r][c]


def calc_HP(dungeon):
    """
    Bottom-up dynamic programming solution.

    Paramters
    ---------
    dungeon : Input matrix
    """

    m = len(dungeon)
    n = len(dungeon[0])

    dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
    dp[m][n - 1] = dp[m - 1][n] = 0

    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            dp = max(min(dp[r][c + 1], dp[r + 1][c]), 0)

    return dp[0][0] + 1
