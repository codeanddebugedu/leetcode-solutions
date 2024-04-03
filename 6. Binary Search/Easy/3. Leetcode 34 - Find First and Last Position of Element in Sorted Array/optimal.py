from typing import List

"""
Time complexity -> O(2 * logN) -> O (logN)
N is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, searching_left):
            low = 0
            high = len(nums) - 1
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    index = mid
                    if searching_left:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return index

        left = binarySearch(nums, target, True)
        if left == -1:
            return [-1, -1]
        right = binarySearch(nums, target, False)
        return [left, right]
