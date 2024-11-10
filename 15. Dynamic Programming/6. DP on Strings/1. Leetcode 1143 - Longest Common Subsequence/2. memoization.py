"""
Time Complexity: O(N*M)
Reason: There are N*M states therefore at max 'N*M' new problems will be solved.

Space Complexity: O(N*M) + O(N+M)
Reason: We are using an auxiliary recursion stack space(O(N+M))
and a 2D array ( O(N*M)).
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
            p1 = self.solve(s1, s2, ind1 - 1, ind2, dp)
            p2 = (self.solve(s1, s2, ind1, ind2 - 1, dp),)
            dp[ind1][ind2] = max(p1, p2)
            return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.solve(text1, text2, n - 1, m - 1, dp)
