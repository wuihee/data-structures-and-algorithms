"""
576. Out of Boundary Paths

Given the five integers m, n, maxMove, startRow, startColumn, return the number
of paths to move the ball out of the grid boundary.
"""

from functools import cache


def find_paths(m, n, maxMove, startRow, startColumn):
    mod = (10 ** 9 + 7)
    
    @cache
    def aux(r, c, moves_left):
        # Base case 1: boundary exceeded.
        if r < 0 or r == m or c < 0 or c == n:
            return 1
        
        # Base case 2: no moves left.
        if moves_left == 0:
            return 0
        
        moves_left -= 1
        up = aux(r + 1, c, moves_left)
        down = aux(r - 1, c, moves_left)
        left = aux(r, c - 1, moves_left)
        right = aux(r, c + 1, moves_left)
        return (up + down + left + right) % mod
    
    return aux(startRow, startColumn, maxMove)
