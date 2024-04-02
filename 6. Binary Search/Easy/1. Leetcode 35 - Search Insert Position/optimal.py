from typing import List

"""
Time complexity -> O(logn)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
