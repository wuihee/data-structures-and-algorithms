"""
The Knight's Tour

Given an N x N board with the Knight placed on the first square of the empty
board, moving according to the rules of chess, the Knight must visit each
square exactly once. Output the order of each square that was visited.
"""

N = 5


def is_safe(x: int, y: int, board) -> bool:
    """
    Utility function to check if square with coordinates x and y is valid.

    Parameters
    ----------
    x : x position of the square we want to check.
    y : y position of the square we want to check.
    board : Current chessboard.
    """
    if x >= 0 and y >= 0 and x < N and y < N and board[x][y] == -1:
        return True
    return False


def print_solution(board: list) -> None:
    """
    A utility function to print chessboard matrix.

    Parameters
    ----------
    board : Chessboard with the solution
    """
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def knights_tour(n, board, curr_x, curr_y, moves):
    """
    A recursive utility function to solve the Knight's Tour problem.

    Parameters:
    -----------
    n : Length of board
    board : 2D matrix where the value of board[i][j] tells us whether or not
            the knight has travelled to the current square.
    curr_x : The current x position of the knight.
    curr_y : The current y position of the knight.
    moves : The number of moves the knight has made so far.
    """

    # move_x and move_y define next move of the Knight.
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # If the position of the knight is one the last square of the board.
    if moves == n ** 2:
        return True

    # Try all next moves from the current coordinate x, y.
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = moves

            if knights_tour(n, board, new_x, new_y, moves + 1):
                return True

            # Backtracking: If we didn't return True, it means moving to this
            # current square is not correct. Therefore, we need to try another
            # square and change the value of this square back to -1 to indicate
            # that we haven't been here.
            board[new_x][new_y] = -1

    return False


def knights_tour_aux(n):
    """
    Begin solving the Knight's Tour problem.

    Parameters
    ----------
    n : length of board.
    """

    # Initialize board matrix.
    board = [[-1 for i in range(n)] for i in range(n)]

    # Knight is initially at the first block.
    board[0][0] = 0

    # Step counter for Knight's position.
    moves = 1

    # Checking if solution exists.
    if not knights_tour(n, board, 0, 0, moves):
        print('Solution does not exist.')
    else:
        print_solution(n, board)


knights_tour_aux(N)
