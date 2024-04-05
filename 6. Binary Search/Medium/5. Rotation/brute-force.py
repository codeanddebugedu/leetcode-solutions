from typing import List

"""
Time complexity -> O(N)
Here, N = size of the given array.

Space complexity -> O(1)
"""


def findKRotation(nums: List[int]) -> int:
    n = len(nums)
    ans = float("inf")
    index = -1
    for i in range(n):
        if nums[i] < ans:
            ans = nums[i]
            index = i
    return index
