"""
Rat in a Maze

Given an N x N maze matrix filled with 0s and 1s, where a 0 represents a dead
end and 1 represents a path, find a path from the top left corner to the bottom
right corner. The rat can only move rightwards and downwards.
"""


def solve_maze(maze, solution_maze, row, col):
    """
    Recursive function to solve rat in a maze problem.

    Parameters
    ----------
    maze : Matrix representing the maze.
    solution_maze : Maps current path that has been travelled so far.
    row : Current y position in the maze.
    col : Current x position in the maze.
    """

    N = len(maze)
    
    # Base Case: End point reached.
    if row == N - 1 and col == N - 1:
        return True

    # Try going right.
    if col < N and maze[row][col + 1] == 1:

        # Indicate that rat has travelled right in the solution.
        solution_maze[row][col + 1] = 1

        # Recursively check if the next move after moving right leads to a
        # solution.
        if solve_maze(maze, solution_maze, row, col + 1):
            return True

        # If no solution was found, backtrack.
        solution_maze[row][col + 1] = 0

    # Try going down.
    if row < N and maze[row + 1][col] == 1:

        # Indicate that rat has travelled down in the solution.
        solution_maze[row + 1][col] = 1

        # Recursively check if the next move after moving down leads to a
        # solution.
        if solve_maze(maze, solution_maze, row + 1, col):
            return True

        # If no solution was found, backtrack.
        solution_maze[row + 1][col] = 0

    # Neither going right or down finds a solution.
    return False


def solve_maze_aux(maze):
    """
    Auxilliary function to the main recursive solution.

    Parameters
    ----------
    maze : Matrix representing the maze.
    """

    N = len(maze)
    solution_maze = [[0 for _ in range(N)] for _ in range(N)]

    # Start at 0,0.
    solution_maze[0][0] = 1

    if solve_maze(maze, solution_maze, 0, 0):
        for i in solution_maze:
            print(i)
    else:
        print('No solution found.')


maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]
solve_maze_aux(maze)
