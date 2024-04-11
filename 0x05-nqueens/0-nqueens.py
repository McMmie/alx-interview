#!/usr/bin/env python3
import sys

solutions = []  # The list of possible solutions to the N queens problem
n = 0  # The size of the chessboard
pos = None  # The list of possible positions on the chessboard


def get_input():
    """
    Retrieves and validates the program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        sys.exit("Usage: nqueens N")
    try:
        n = int(sys.argv[1])
    except Exception:
        sys.exit("N must be a number")
    if n < 4:
        sys.exit("N must be at least 4")
    return n


def is_attacking(pos0, pos1):
    """
    Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    return (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]) or (abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))


def group_exists(group):
    """
    Checks if a group exists in the list of solutions.

    Args:
        group (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        if all(stn_pos in group for stn_pos in stn):
            return True
    return False


def build_solution(row, group):
    """
    Builds a solution for the N queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions, n
    if row == n:
        tmp0 = group[:]
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip([pos[a]] * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a][:])
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop()


def get_solutions():
    """Gets the solutions for the given chessboard size."""
    global pos, n
    pos = [[x // n, x % n] for x in range(n ** 2)]
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)

