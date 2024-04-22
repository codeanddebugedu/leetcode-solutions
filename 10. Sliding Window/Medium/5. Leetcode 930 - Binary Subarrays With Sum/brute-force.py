from typing import List

"""
Time complexity -> O(N^2)
N is the number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total > goal:
                    break
                if total == goal:
                    count += 1
        return count
