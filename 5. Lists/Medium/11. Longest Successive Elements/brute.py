from typing import *

"""
Time complexity -> O(N^2)
N is number of elements in nums

Space complexity -> O(1)
"""


def longestSuccessiveElements(arr: List[int]) -> int:
    max_count = 0
    n = len(arr)
    for i in range(0, n):
        num = arr[i]
        count = 1
        while num + 1 in arr:
            count += 1
            num += 1
        max_count = max(max_count, count)
    return max_count
