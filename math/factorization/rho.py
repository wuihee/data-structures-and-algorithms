"""
Pollard's Rho Algorithm

An Integer factorization algorithm that relies on the birthday paradox and
Floyd's cycle detection algorithm.

https://www.cs.colorado.edu/~srirams/courses/csci2824-spr14/pollardsRho.html
http://www.geeksforgeeks.org/pollards-rho-algorithm-prime-factorization/
https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
"""

import math
import random


def rho(dividend):
    """
    Employs Pollard's rho and Floyd's cycle finding algorithm to find the
    factors of dividend.
    """
    a = int(random.random() * 100)  # Random number between 1 and 100.
    f = lambda x: (x ** 2 + a) % dividend  # Pseudorandom number generator.
    n1 = f(2)  # Tortoise: starts at 2 and takes 1 step.
    n2 = f(n1)  # Hare: takes 1 step from tortoise.
    gcd_val = 1  # Value of gcd(n1 - n2, dividend).

    while gcd_val == 1:  # While abs(n1 - n2) is not congruent to dividend.
        gcd_val = math.gcd(abs(n1 - n2), dividend)
        n1 = f(n1)  # Moves 1 step.
        n2 = f(f(n2))  # Moves 2 steps.

    return gcd_val


if __name__ == "__main__":
    dividend = int(input("Enter a number to be factorized: "))
    factor = rho(dividend)
    print(factor)
