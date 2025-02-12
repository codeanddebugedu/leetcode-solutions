from typing import List

"""
Time complexity -> O(2 * logN) -> O (logN)
N is number of elements in nums

Space complexity -> O(1)
"""


# Solution 1
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


# ---------------------------------------
# Solution 2
def xyz():
    print("Hello")


class Solution:
    def binarySearchLeft(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index

    def binarySearchRight(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ext_left = self.binarySearchLeft(nums, target)
        if ext_left == -1:
            return [-1, -1]
        ext_right = self.binarySearchRight(nums, target)
        return [ext_left, ext_right]
