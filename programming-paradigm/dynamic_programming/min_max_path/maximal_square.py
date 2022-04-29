"""
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.
"""


def max_square_naive(matrix):
    """
    Naive recursive solution.

    Parameters
    ----------
    matrix : Input matrix.
    """

    def aux(r, c):
        """
        Auxilliary function to help check for square of 1's.

        Parameters
        ----------
        r : Position of current row.
        c : Position of current column.
        """
    
        nonlocal m, n
        if r < m and c < n:
            if matrix[r][c] == 1:
                return min(aux(r + 1, c), aux(r, c + 1), aux(r + 1, c + 1)) + 1
        return 0

    m = len(matrix)
    n = len(matrix[0])
    max_side = 0

    for r in range(m):
        for c in range(n):

            # If current cell is a '1', start check for a square of 1's.
            if matrix[r][c] == '1':
                length = aux(r, c)
                max_side = max(max_side, length)

    return max_side ** 2


def max_square_rec(matrix):
    """
    Recursive dynamic programming solution.

    Paramters
    ---------
    matrix : Input matrix.
    """

    def aux(r, c):
        """
        Auxilliary function to help check for square of 1's.

        Parameters
        ----------
        r : Position of current row.
        c : Position of current column.
        """
    
        nonlocal m, n, dp
        if r < m and c < n:
            if dp[r][c] != -1:
                return dp[r][c]
            if matrix[r][c] == '1':
                dp[r][c] = min(aux(r + 1, c), aux(r, c + 1),
                               aux(r + 1, c + 1)) + 1
            else:
                dp[r][c] = 0
            return dp[r][c]
        return 0

    m = len(matrix)
    n = len(matrix[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    max_side = 0

    for r in range(m):
        for c in range(n):

            # If current cell is a '1', start check for a square of 1's.
            if matrix[r][c] == '1':
                length = aux(r, c)
                max_side = max(max_side, length)

    return max_side ** 2


def max_square(matrix):
    """
    Iterative dyanmic programming solution.

    Paramters
    ---------
    matrix : Input matrix
    """

    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0

    # dp[r][c] represents the
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    max_side = 0

    for r in range(1, m + 1):
        for c in range(1, n + 1):

            # If current cell is '1'
            if matrix[r - 1][c - 1] == '1':

                # '1' will be at the bottom right corner of the 4 squares.
                # Recurrence equation will check all the other squares.
                dp[r][c] = min(dp[r][c - 1], dp[r - 1][c],
                               dp[r - 1][c - 1]) + 1
                max_side = max(max_side, dp[r][c])

    return max_side ** 2
