#!/usr/bin/python3
"""
making change
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Calculate the minimum number of coins
    needed to make the given total amount.

    Args:
    - coins (List[int]): A list of coin denominations available.
    - total (int): The target total amount to make.

    Returns:
    - int: The minimum number of coins needed to make the total amount.
           Returns -1 if it's not possible to
           make the total amount with the given coins.
    """

    if total <= 0:
        return 0

    # Initialize an array to store the minimum
    # number of coins needed to make each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update the minimum number of coins needed for each amount
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return the minimum number of coins needed to make the total amount
    return min_coins[total] if min_coins[total] != float('inf') else -1
