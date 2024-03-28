from typing import *

"""
Time complexity -> O(N^2)
N is number of elements in nums

Space complexity -> O(1)
"""


def linearSearch(arr, num):
    for i in arr:
        if i == num:
            return True
    return False


def longestSuccessiveElements(arr: List[int]) -> int:
    max_count = 0
    for i in arr:
        x = i
        count = 1
        while linearSearch(arr, x + 1):
            x += 1
            count += 1
        max_count = max(max_count, count)
    return max_count
