from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        # Initialize dp array where dp[i] represents the minimum jumps to reach the last index from index i
        dp = [float("inf")] * n
        dp[n - 1] = (
            0  # Base case: 0 jumps needed to reach the end if we're already there
        )

        # Fill the dp array from the second last index to the first index
        for i in range(n - 2, -1, -1):
            furthest_jump = min(i + nums[i], n - 1)
            for j in range(i + 1, furthest_jump + 1):
                dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]
