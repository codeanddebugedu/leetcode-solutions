from typing import List

"""
Time complexity -> O(logN)
N is the number of elements in nums

Space complexity -> O(logN) (Stack Space)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive(nums, low, high, target):
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return recursive(nums, mid + 1, high, target)
            else:
                return recursive(nums, low, mid - 1, target)

        return recursive(nums, 0, len(nums) - 1, target)
