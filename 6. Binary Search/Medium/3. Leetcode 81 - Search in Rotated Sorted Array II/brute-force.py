from typing import List

"""
Time complexity -> O(N)
N is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False
