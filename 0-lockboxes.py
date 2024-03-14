#!/usr/bin/python3
"""
documentation
"""

from collections import deque


def canUnlockAll(boxes):
    """
    documentation
    """


    n = len(boxes)
    visited = set([0])
    unvisited = set(boxes([0]).difference(set([0]))

    while len(unvisited) > 0:
        current_box = unvisited.pop()
        if not current_box or current_box >= n:
            continue
        if current_box not in visited:
            unvisited = unvisited.union(boxes[current_box])
            visited.add(current_box)

    return n == (visited)
