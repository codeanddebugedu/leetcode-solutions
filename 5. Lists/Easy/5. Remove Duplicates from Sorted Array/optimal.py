from typing import List

"""
Time complexity = O(n) where n is the number of elements in list
But in this case, we are using only 1 loop instead of 2 FOR loops

Space complexity = O(1), no extra space
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        return i + 1
