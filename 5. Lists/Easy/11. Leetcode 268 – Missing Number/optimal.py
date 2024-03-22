from typing import List

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        original_total = (n * (n + 1)) // 2
        return original_total - sum(nums)
