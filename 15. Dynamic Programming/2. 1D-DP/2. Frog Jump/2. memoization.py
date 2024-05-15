"""
Time Complexity: O(N)
Reason: The overlapping subproblems will return the answer in constant time O(1). 
Therefore the total number of new subproblems we solve is 'n'. 
Hence total time complexity is O(N).

Space Complexity: O(N)
Reason: We are using a recursion stack space(O(N)) and an array (again O(N)). 
Therefore total space complexity will be O(N) + O(N) ≈ O(N)
"""


class Solution:
    def energyUsed(self, height, index, dp):
        if index == 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        left = self.energyUsed(height, index - 1, dp) + abs(
            height[index] - height[index - 1]
        )
        right = float("inf")
        if index > 1:
            right = self.energyUsed(height, index - 2, dp) + abs(
                height[index] - height[index - 2]
            )
        dp[index] = min(left, right)
        return dp[index]

    def minimumEnergy(self, height, n):
        dp = [-1] * n
        return self.energyUsed(height, n - 1, dp)
