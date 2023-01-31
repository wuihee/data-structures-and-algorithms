"""
1000. Minimum Cost To Merge Stones

There are n piles of stones arranged in a row. The ith pile has stones[i]
stones. A move consists of merging exactly k consecutive piles into one pile,
and the cost of this move is equal to the total number of stones in these k
piles. Return the minimum cost to merge all piles of stones into one pile. If
it is impossible, return -1.
"""


# Reduce problem: you can only merge two adjacent piles of stones.
def merge_two(stones):
    n = len(stones)

    # dp[i][j] is the min. cost to merge stones from index i to j.
    # Base case: if i == j, return 0.
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = (min(dp[i][k] + dp[k + 1][j] for k in range(i, j)) +
                        sum(stones[i:j + 1]))

    return dp[0][n - 1]


# Original problem: merge k piles.
def merge_stones(stones):
    n = len(stones)
    dp = [[[[0] * n] for _ in range(n)] for _ in range(n)]

    # Base case: dp[i][i][1] = 0; only 1 pile.
    for i in range(n):
        dp[i][i][1] = 0

    
