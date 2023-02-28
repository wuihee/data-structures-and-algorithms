"""
Prime Factorization

Very basic prime factorization algorithm that can be coded on the fly.
"""

import math

def prime_factors(n):
    """
    Return all prime factors of n.

    Parameters
    ----------
    n - Number which you wish to factorize.
    """

    factors = []

    # Start by dividing n by 2 while i can.
    while n % 2 == 0:
        n //= 2
        factors.append(2)

    # Now, n is odd and we check all numbers from 3 to the square root of n.
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i
            factors.append(i)

    # If n > 2, it means that the remaining number is the last prime factor.
    if n > 2:
        factors.append(n)

    return factors
