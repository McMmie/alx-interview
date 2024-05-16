#!/usr/bin/python3
"""
"""


def isWinner(x, nums):
    """
    """
    if x < 1 or not nums:
        return None

    # Sieve of Eratosthenes to find all primes up to the maximum number in num
    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    p = 2
    while p * p <= max_n:
        if sieve[p]:
            for i in range(p * p, max_n + 1, p):
                sieve[i] = False
        p += 1

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(sieve[:n+1])

        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
