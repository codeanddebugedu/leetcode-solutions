from typing import List

"""
Time complexity -> O(n logn)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
