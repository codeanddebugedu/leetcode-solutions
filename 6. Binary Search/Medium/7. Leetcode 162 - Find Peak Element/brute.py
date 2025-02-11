from typing import List

"""
Time complexity -> O(N)
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[n - 1] > nums[n - 2]:
            return n - 1
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
