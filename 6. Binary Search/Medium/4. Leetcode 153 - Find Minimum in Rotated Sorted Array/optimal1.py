from typing import List

"""
Time complexity -> O(logN)
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        minimum = float("inf")
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                minimum = min(minimum, nums[low])
                low = mid + 1
            else:
                minimum = min(minimum, nums[mid])
                high = mid - 1
        return minimum
