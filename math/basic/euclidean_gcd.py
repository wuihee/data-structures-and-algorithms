"""
Euclidean Algorithm for Finding Greatest Common Denominator

Given two integers a and b, find the greatest common demoniator.
I.e. the largest number that can divide both a and b.

The Euclidean algorithm is based on the principle that the greatest common
divisor of two numbers does not change if the larger number is replaced by
its difference with the smaller number.
"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
