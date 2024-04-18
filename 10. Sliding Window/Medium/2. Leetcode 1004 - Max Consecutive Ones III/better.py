"""
Time complexity -> O(N) + O(N) -> O(2N)
N is the number of nodes

Space complexity -> O(1)
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = 0
        right = 0
        zeros = 0
        n = len(nums)
        while right < n:
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                length = right - left + 1
                max_length = max(max_length, length)
            right += 1
        return max_length
