"""
Time Complexity: O(N*N)
Space Complexity: O(N*N) + O(N+N)
Reason: We are using an auxiliary recursion stack space(O(N+N))
and a 2D array ( O(N*N)).
"""


class Solution:
    def solve(self, s1, s2, ind1, ind2, dp):
        if ind1 < 0 or ind2 < 0:
            return 0
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]
        if s1[ind1] == s2[ind2]:
            return 1 + self.solve(s1, s2, ind1 - 1, ind2 - 1, dp)
        else:
            dp[ind1][ind2] = max(
                self.solve(s1, s2, ind1 - 1, ind2, dp),
                self.solve(s1, s2, ind1, ind2 - 1, dp),
            )
            return dp[ind1][ind2]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.solve(s, s[::-1], n - 1, n - 1, dp)
