"""
Time Complexity: O(2 ^ (m x n))
Space Complexity: O(M-1) + O(N-1)
"""


class Solution:
    def solve(self, i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        up = self.solve(i - 1, j)
        left = self.solve(i, j - 1)
        return up + left

    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(m - 1, n - 1)
