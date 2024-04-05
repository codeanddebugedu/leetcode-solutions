from typing import List

"""
Time complexity -> O(logN)
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        low = 1
        high = len(nums) - 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1
