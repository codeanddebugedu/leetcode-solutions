from typing import List

"""
Time complexity -> O(logN)
N is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
