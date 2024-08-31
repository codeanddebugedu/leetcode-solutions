from typing import List


class Solution:
    def solve(self, index, jump, lastIndex, nums):
        if index >= lastIndex:
            return jump
        minJump = float("inf")
        for i in range(1, nums[index] + 1):
            minJump = min(minJump, self.solve(index + i, jump + 1, lastIndex, nums))
        return minJump

    def jump(self, nums: List[int]) -> int:
        return self.solve(0, 0, len(nums) - 1, nums)
