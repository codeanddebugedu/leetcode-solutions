"""
Precise Time Complexity: O(2^(n*n)), 

Space Complexity: O(n+n) + O(n+n)
Reason: We are using an auxiliary recursion stack space(O(N+M)) and a 2D array ( O(N*M)).
"""


class Solution:
    def solve(self, s1, s2, ind1, ind2):
        if ind1 < 0 or ind2 < 0:
            return 0
        if s1[ind1] == s2[ind2]:
            return 1 + self.solve(s1, s2, ind1 - 1, ind2 - 1)
        else:
            return max(
                self.solve(s1, s2, ind1 - 1, ind2), self.solve(s1, s2, ind1, ind2 - 1)
            )

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve(text1, text2, len(text1) - 1, len(text2) - 1)
