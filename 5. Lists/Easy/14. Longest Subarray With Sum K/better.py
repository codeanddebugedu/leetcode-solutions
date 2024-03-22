from sys import *
from collections import *
from math import *

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(n)
"""


def getLongestSubarray(nums: [int], k: int) -> int:
    sum_map = dict()
    Sum = 0
    max_length = 0
    for i in range(0, len(nums)):
        Sum += nums[i]
        if Sum == k:
            max_length = i + 1

        rem = Sum - k
        if rem in sum_map:
            l = i - sum_map[rem]
            max_length = max(max_length, l)

        if Sum not in sum_map:
            sum_map[Sum] = i

    return max_length
