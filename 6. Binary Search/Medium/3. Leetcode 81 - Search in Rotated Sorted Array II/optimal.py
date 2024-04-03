from typing import List

"""
Time complexity -> O(logN) for the best and average case. O(N/2) for the worst case. 
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                high -= 1
                low += 1
                continue
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

        return False
