"""
790. Domino and Tromino Tiling

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may
rotate these shapes. Given an integer n, return the number of ways to tile an
2 x n board. Since the answer may be very large, return it modulo 109 + 7.
"""


def tile_board_rec(n):
    def aux(i, prev_gap):
        """Return the number of ways to fill up the board from column 0 to i."""

        # Base case 1: last column exceeded
        if i > n:
            return 0
        
        # Base case 2: last column reached
        if i == n:
            return 1 if not prev_gap else 0
        
        # If previous column is completely filled.
        if not prev_gap:
            # 1. place verticle domino.
            res_1 = aux(i + 1, False)
            # 2. Place two horizontal dominos.
            res_2 = aux(i + 2, False)
            # 3. Place trominos in two directions.
            res_3 = aux(i + 2, True)
            return res_1 + res_2 + res_3 * 2
            
        # If previous gap is unfilled.
        if prev_gap:
            # 1. Place tromino.
            res_1 = aux(i + 1, False)
            # 2. Place horizontal domino.
            res_2 = aux(i + 1, True)
            return res_1 + res_2
            
    return aux(0, False)


def tile_board(n):
    """Bottom-up solution."""
    dp = [[0, 0] for _ in range(n + 2)]

    # Base cases.
    dp[1] = [1, 1]
    dp[2] = [2, 2]

    for i in range(3, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 2][1]
        dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

    return dp[n][0] % (10 ** 9 + 7)
