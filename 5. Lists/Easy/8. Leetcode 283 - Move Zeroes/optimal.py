from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        else:
            return
        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
