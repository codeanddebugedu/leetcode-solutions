"""
Time complexity -> O(N)
N is the number of elements in nums

Space complexity -> O(1)
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        n = len(nums)
        zeros = 0
        max_length = 0
        while right < n:
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                length = right - left + 1
                max_length = max(max_length, length)
            right += 1
        return max_length
