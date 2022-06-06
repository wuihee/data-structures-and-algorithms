"""
Edit Distance

Given two strings, S1 and S2, return the minimum number of operations required
to convert S1 into S2. The operations are: insert, delete, replace.
"""


from functools import cache


def edit_distance_rec(S1, S2):

    @cache
    def aux(i, j):
        # Base cases.
        if i == -1 and j == -1:
            return 0
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        # Both current characters are the same.
        if S1[i] == S2[j]:
            return aux(i - 1, j - 1)
        
        insert = aux(i, j - 1)
        delete = aux(i - 1, j)
        replace = aux(i - 1, j - 1)
        
        return min(insert, delete, replace) + 1

    return aux(len(S1) - 1, len(S2) - 1)


def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base case.
    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # Match.
            if word1[i - 1] == word2[j - 1]:
                table[i][j] = table[i - 1][j - 1]

            else:
                mismatch = table[i - 1][j - 1]
                insert = table[i][j - 1]
                delete = table[i - 1][j]
                table[i][j] = 1 + min(mismatch, insert, delete)

    return table[-1][-1]
        
