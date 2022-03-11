"""
N-Queens Problem

Given an N x N chessboard, find a way to place N queens on the chessboard such
that none of them are attacking one another.
"""


def is_safe(board, row, col):
    """
    Helper function to check if square with coordinates x, y is safe.

    Parameters
    ----------
    board : Current state of chessboard.
    col : x position of square we want to check.
    row : y position of square we want to check.
    """

    N = len(board)
    
    # Check for queens above.
    for r in range(row):
        if board[r][col] == 'Q':
            return False

    # Check upper-left diagonal.
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[r][c] == 'Q':
            return False

    # Check upper-right diagonal.
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[r][c] == 'Q':
            return False

    return True


def queens_aux(N):
    """
    Auxilliary function to help start N-Queens problem.

    Parameters
    ----------
    N : The width of the N x N chessboard.
    """

    # Initialize chessboard.
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Start on row 0.
    if n_queens(board, 0):
        for row in board:
            print(row)
    else:
        print('A solution was not found.')


def n_queens(board, row):
    """
    Main recursive function to solve N-Queens problem.

    Parameters
    ----------
    board : Current state of chessboard.
    row : Current row to place the next queen on.
    queens : The number of queens that have been placed.
    """

    N = len(board)

    # Base Case: All queens have already been placed.
    if row >= N:
        return True

    # For each empty column in this row, try placing a queen and recursively
    # check if the solution is correct.
    for col in range(N):

        # If queen is not under attack from any other queens, place a queen
        # in the current square.
        if is_safe(board, row, col):
            board[row][col] = 'Q'

            # Recursively search for a solution in the next row. Returns
            # True if a solution was found.
            if n_queens(board, row + 1):
                return True

            # Backtrack: If solution was incorrect and returned False, it is
            # incorrect to place a queen in the current square. Therefore,
            # backtrack and change it's value back to -1.         
            board[row][col] = -1

    # Return False when no queen could be placed on any column in this row.
    return False


print(queens_aux(5))
