from typing import List

"""
Time complexity -> O(n^2)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
