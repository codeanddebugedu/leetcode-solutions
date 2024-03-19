"""
Time complexity = O(N) where N is the number of elements in list
Because we looping through the array only once

Space complexity = O(1)
"""

from typing import List


def isSorted(n: int, a: List[int]) -> int:
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]:
            return 0
    return 1
