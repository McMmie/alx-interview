#!/usr/bin/python3
"""
a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    operations = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            operations += min_ops
            n = n / min_ops
        min_ops += 1
    return operations
