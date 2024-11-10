"""
Time Complexity: O(N*M)
Reason: There are two nested loops

Space Complexity: O(N*M)
Reason: We are using an external array of size 'N*M'. Stack Space is eliminated.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(m + 1):
            dp[0][j] = 0
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    p1 = dp[ind1 - 1][ind2]
                    p2 = dp[ind1][ind2 - 1]
                    dp[ind1][ind2] = max(p1, p2)
        return dp[n][m]
