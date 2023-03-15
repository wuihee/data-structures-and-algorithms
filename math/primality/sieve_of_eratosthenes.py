# Sieve of Eratosthenes


def sieve(N):
    """
    Uses the sieve of eratosthenes to return a list of prime numbers from range
    2 to 'N'.
    """
    prime = 2
    numbers = list(range(2, N))
    remaining = numbers.copy()

    while remaining:
        # Remove all multiples of 'prime' in 'numbers'.
        for i in range(prime, N - prime, prime):
            numbers[i] = 0

        # Get the next biggest number.
        remaining = [i for i in numbers if i > prime]
        if remaining:
            prime = remaining[0]

    return [i for i in numbers if i != 0]


print(sieve(100))
