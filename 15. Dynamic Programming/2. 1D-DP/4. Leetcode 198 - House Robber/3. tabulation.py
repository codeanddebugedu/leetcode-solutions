"""
Time Complexity: O(N)
Reason: We are running a simple iterative loop

Space Complexity: O(N)
Reason: We are using an external array of size 'n+1'.
"""

from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        for index in range(1, n):
            pick = nums[index]
            if index > 1:
                pick += dp[index - 2]
            notpick = 0 + dp[index - 1]
            dp[index] = max(pick, notpick)
        return dp[n - 1]
