"""
Time Complexity: O(N*K)
Reason: The overlapping subproblems will return the answer in constant time. 
Therefore the total number of new subproblems we solve is 'n'. 
At every new subproblem, we are running another loop for K times. 
Hence total time complexity is O(N * K).

Space Complexity: O(N)
Reason: We are using a recursion stack space(O(N)) and an array (again O(N)). 
Therefore total space complexity will be O(N) + O(N) ≈ O(N)
"""


class Solution:
    def solveQ(self, index, height, k, dp):
        if index <= 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        minimum_steps = float("inf")
        for j in range(1, k + 1):
            if index - j >= 0:
                jump = self.solveQ(index - j, height, k, dp) + abs(
                    height[index] - height[index - j]
                )
                minimum_steps = min(minimum_steps, jump)
        dp[index] = minimum_steps
        return dp[index]

    def minimizeCost(self, height, n, k):
        dp = [-1] * n
        return self.solveQ(n - 1, height, k, dp)
