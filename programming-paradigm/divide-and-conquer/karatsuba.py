"""Karatsuba's Algorithm for Polynomial Multiplication"""


def add_lists(L1, L2):
    """
    Given lists L1 and L2, add them together starting from the last in-
    dex.
    """

    L1, L2 = sorted((L1, L2), key=len)
    length_1, length_2 = len(L1), len(L2)

    if length_1 < length_2:
        L1 = [0 for i in range(length_2 - length_1)] + list(L1)

    return [sum(i) for i in zip(L1, L2)]


def substract_lists(L1, L2):
    """
    Subtract the values of L2 from L1, starting from the last index.
    """
    for i in range(-1, -len(L2) - 1, -1):
        L1[i] -= L2[i]

    return L1


def remove_zeros(L):
    """Given a list 'L', remove all zeros in front."""
    while not L[0]:
        L = L[1:]

    return L


def karatsuba(A, B):
    """
    Fast multiplication algorithm. In this implementation, return the
    product of polynomials 'A * B'.
    """
    n = len(A)
    m = len(B)
    resultant = [0 for i in range(n + m - 1)]

    # Base Case: Multiply out 'A' and 'B' when either 'n' or 'm' is 1.
    if n == 1 or m == 1:
        resultant = []
        for i in A:
            for j in B:
                resultant.append(i * j)
        return resultant

    # Divide
    a1 = A[:n // 2]
    a0 = A[n // 2:]
    b1 = B[:m // 2]
    b0 = B[m // 2:]

    # 'a1_b1' and 'a0_b0'.
    a1_b1 = karatsuba(a1, b1)
    a0_b0 = karatsuba(a0, b0)

    # Middle: '(a1 + a0) * (b1 + b0) - a1_b1 - a0_b0'
    a = add_lists(a1, a0)
    b = add_lists(b1, b0)
    a_b = karatsuba(a, b)
    a_b = substract_lists(a_b, a1_b1)
    a_b = substract_lists(a_b, a0_b0)
    a_b = remove_zeros(a_b)  # Remove zeros at the front of the list.

    # Add 'a1_b1' to 'resultant', starting from index 0.
    for i in range(len(a1_b1)):
        resultant[i] += a1_b1[i]

    # Add 'a0_b0' to 'resultant' starting from the last index.
    for i in range(-1, -len(a0_b0) - 1, -1):
        resultant[i] += a0_b0[i]

    # Add 'a_b' to resultant.
    for i in range(len(a_b)):
        resultant[max(n, m) // 2 + i] += a_b[i]

    return resultant
"""Naive Polynomial Multiplication"""


def remove_zeros(L):
    """Given a list 'L', remove all zeros in front."""
    while not L[0]:
        L = L[1:]

    return L


def multiply_polynomial(A, B):
    """
    Give 2 polynomials A and B, and their respective lengths n, find the
    product polynomial. Runtime: O(n) = n^2.
    """
    n = len(A)
    m = len(B)
    product = [0 for i in range(n + m - 1)]

    for a in range(n):
        for b in range(m):
            product[a + b] += A[a] * B[b]

    return remove_zeros(product)
"""Naive Divide and Conquer Algorithm for Polynomial Multiplication"""


def remove_zeros(L):
    """Given a list 'L', remove all zeros in front."""
    while not L[0]:
        L = L[1:]

    return L


def multiply_polynomial(A, B):
    """
    Given polynomials (lists) 'A' and 'B', find the resultant polynomi-
    al of 'A * B'. Runtime: O(n) = n^2. Prerequisite for Karatsuba's a-
    lgorithm.

    Will not work if the first terms of 'A' and 'B' are zeros.
    """
    n = len(A)
    m = len(B)
    resultant = [0 for i in range(n + m - 1)]

    # Base Case: Multiply out if either 'A' or 'B' only has 1 term.
    if n == 1 or m == 1:
        resultant = []
        for i in A:
            for j in B:
                resultant.append(i * j)
        return resultant

    # Divide Polynomials
    a1 = A[:n // 2]
    a0 = A[n // 2:]
    b1 = B[:m // 2]
    b0 = B[m // 2:]

    a1_b1 = multiply_polynomial(a1, b1)
    a0_b0 = multiply_polynomial(a0, b0)
    a1_b0 = multiply_polynomial(a1, b0)
    a0_b1 = multiply_polynomial(a0, b1)

    # Update Final Product
    # Add 'a1 * b1', starting at the beginning (index 0).
    for i in range(len(a1_b1)):
        resultant[i] += a1_b1[i]
    # Add 'a0 * b0', starting from the end (index -1).
    for i in range(-1, -len(a0_b0) - 1, -1):
        resultant[i] += a0_b0[i]
    # Add 'a1 * b0', starting at index m / 2.
    for i in range(len(a1_b0)):
        resultant[m // 2 + i] += a1_b0[i]
    # Add 'a1 * b0', starting at index n / 2.
    for i in range(len(a0_b1)):
        resultant[n // 2 + i] += a0_b1[i]

    return remove_zeros(resultant)
