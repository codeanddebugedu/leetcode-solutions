"""
Time Complexity: O(N)
Reason: We are running a simple iterative loop

Space Complexity: O(N)
Reason: We are using an external array of size 'n+1'.
"""


class Solution:
    def minimumEnergy(self, height, n):
        dp = [-1] * n
        dp[0] = 0
        for i in range(1, n):
            jump2 = float("inf")
            jump1 = dp[i - 1] + abs(height[i] - height[i - 1])
            if i > 1:
                jump2 = dp[i - 2] + abs(height[i] - height[i - 2])
            dp[i] = min(jump1, jump2)
        return dp[n - 1]
