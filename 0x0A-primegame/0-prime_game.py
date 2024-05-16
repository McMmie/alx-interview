#!/usr/bin/python3
"""
"""


def isWinner(x, nums):
    """Function to determine the winner of each game."""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(max_n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, max_n + 1, p):
                is_prime[multiple] = False

    primes_up_to = [i for i, prime in enumerate(is_prime) if prime]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [p for p in primes_up_to if p <= n]

        move_count = 0
        remaining = [True] * (n + 1)

        for prime in primes:
            if remaining[prime]:
                move_count += 1
                for multiple in range(prime, n + 1, prime):
                    remaining[multiple] = False

        if move_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
