"""
474. Ones and Zeros

You are given an array of binary strings strs and two integers m and n. Return
the size of the largest subset of strs such that there are at most m 0's and n
1's in the subset.
"""


def largest_subset_naive(count, m, n, i):
    """
    Naive recursive solution using the Knapsack 0-1 strategy.
    
    Paramters
    ---------
    count : count[i][0] is the number 0s for the ith subset, etc.
    m : Minimum number of 0's.
    n : Minimum number of 1's.
    i : Current string.
    """

    # Base case: if there are no more ones or zeros to use.
    if m == 0 and n == 0:
        return 0
    
    # Base case: if the last element is reached.
    if i == len(count):
        return 0
    
    # Number of ones and zeros in the current subset.
    zeros = count[i][0]
    ones = count[i][1]

    # Include current item.
    subset_1 = 0
    if zeros <= m and ones <= n:
        subset_1 = largest_subset_naive(count, m - zeros, n - ones, i + 1) + 1
        
    # Don't include current item.
    subset_2 = largest_subset_naive(count, m, n, i + 1)
    
    return max(subset_1, subset_2)


def largest_subset_rec(count, m, n, i, dp):
    # Base case
    if m == 0 and n == 0:
        dp[i, m, n] = 0
        return 0
    
    if i == len(count):
        return 0
    
    if (m, n, i) in dp:
        return dp[m, n, i]
    
    zeros = count[i][0]
    ones = count[i][1]

    # Include current item.
    subset_1 = 0
    if zeros <= m and ones <= n:
        subset_1 = largest_subset_rec(count, m - zeros, n - ones, i + 1, dp) + 1
        
    # Don't include current item.
    subset_2 = largest_subset_rec(count, m, n, i + 1, dp)
    
    dp[m, n, i] = max(subset_1, subset_2)
    return dp[m, n, i]


def largest_subset(strs, m, n):
    x = len(strs)
    count = [[i.count('0'), i.count('1')] for i in strs]
    dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)]
          for _ in range(x + 1)]
    
    for i in range(x + 1):
        ones = count[i - 1][1]
        zeros = count[i - 1][0]

        for j in range(m + 1):
            for k in range(n + 1):
                if i == 0:
                    pass
                elif j >= zeros and k >= ones:
                    dp[i][j][k] = max(dp[i - 1][j][k],
                                      dp[i - 1][j - zeros][k - ones] + 1)
                else:
                    dp[i][j][k] = dp[i - 1][j][k]

    return dp[x][m][n]
