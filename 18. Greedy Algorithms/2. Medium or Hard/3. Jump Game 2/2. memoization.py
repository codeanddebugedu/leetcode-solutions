from typing import List


class Solution:
    def solve(self, index, jump, lastIndex, nums, dp):
        if index >= lastIndex:
            return jump

        if dp[index][jump] != -1:
            return dp[index][jump]

        minJump = float("inf")
        for i in range(1, nums[index] + 1):
            minJump = min(minJump, self.solve(index + i, jump + 1, lastIndex, nums, dp))

        dp[index][jump] = minJump
        return minJump

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]  # Initialize dp array with -1
        return self.solve(0, 0, n - 1, nums, dp)
