from typing import *

"""
Time complexity -> O(NlogN + N)
N is number of elements in nums

Space complexity -> O(1)
"""


def longestSuccessiveElements(arr: List[int]) -> int:
    arr.sort()
    last_smaller = float("-inf")
    count = 0
    longest = 0
    for num in arr:
        if num - 1 == last_smaller:
            count += 1
            last_smaller = num
        elif num != last_smaller:
            count = 1
            last_smaller = num
        longest = max(longest, count)
    return longest
