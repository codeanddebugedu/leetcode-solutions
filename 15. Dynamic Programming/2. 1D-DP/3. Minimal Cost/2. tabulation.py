"""
Time Complexity: O(N*K)
Reason: We are running two nested loops, where outer loops run from 1 to n-1 
and the inner loop runs from 1 to K

Space Complexity: O(N)
Reason: We are using an external array of size 'n'
"""


class Solution:
    def minimizeCost(self, height, n, k):
        dp = [-1] * n
        dp[0] = 0
        for i in range(1, n):
            minimumSteps = float("inf")
            for j in range(1, k + 1):
                if i - j >= 0:
                    jump = dp[i - j] + abs(height[i] - height[i - j])
                    minimumSteps = min(jump, minimumSteps)
            dp[i] = minimumSteps

        return dp[n - 1]
