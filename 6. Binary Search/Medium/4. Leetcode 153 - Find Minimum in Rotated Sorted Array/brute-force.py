from typing import List

"""
Time complexity -> O(N)
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float("inf")
        for i in range(len(nums)):
            minimum = min(minimum, nums[i])
        return minimum
