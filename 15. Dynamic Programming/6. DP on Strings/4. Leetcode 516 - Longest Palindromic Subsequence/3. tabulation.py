"""
Time Complexity: O(N*N)
Reason: There are two nested loops

Space Complexity: O(N*N)
Reason: We are using an external array of size 'N*N'. Stack Space is eliminated.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        text1 = s
        text2 = s[::-1]
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(n + 1):
            dp[0][j] = 0
        for ind1 in range(1, n + 1):
            for ind2 in range(1, n + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(
                        dp[ind1 - 1][ind2],
                        dp[ind1][ind2 - 1],
                    )
        return dp[n][n]
