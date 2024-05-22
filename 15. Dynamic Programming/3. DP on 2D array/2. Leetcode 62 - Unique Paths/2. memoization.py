"""
Time Complexity: O(M*N)
Reason: At max, there will be M*N calls of recursion.

Space Complexity: O((N-1)+(M-1)) + O(M*N)
"""


class Solution:
    def solve(self, i, j, dp):
        if dp[i][j] != -1:
            return dp[i][j]
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        up = self.solve(i - 1, j, dp)
        left = self.solve(i, j - 1, dp)
        dp[i][j] = up + left
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for j in range(n)] for i in range(m)]
        return self.solve(m - 1, n - 1, dp)
