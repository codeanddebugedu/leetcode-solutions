from typing import List

"""
Time Complexity = O(n)
Space Complexity = O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n  # Handle cases where k > n

        reverse(n - k, n - 1)  # Reverse the last k element
        reverse(0, n - k - 1)  # Reverse the remaining elements
        reverse(0, n - 1)  # Reverse the entire array
