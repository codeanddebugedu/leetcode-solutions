from typing import List

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]
