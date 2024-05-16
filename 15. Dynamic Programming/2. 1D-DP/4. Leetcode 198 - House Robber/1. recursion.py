from typing import List


class Solution:
    def solve(self, index, nums):
        if index == 0:
            return nums[index]
        if index == -1:
            return 0
        pick = nums[index] + self.solve(index - 2, nums)
        notpick = 0 + self.solve(index - 1, nums)
        return max(pick, notpick)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.solve(n - 1, nums)
