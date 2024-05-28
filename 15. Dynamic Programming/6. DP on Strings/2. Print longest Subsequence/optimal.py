class Solution:
    def all_longest_common_subsequences(self, s, t):
        n = len(s)
        m = len(t)

        # Initialize dp table
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # Fill dp table
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s[ind1 - 1] == t[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        # Length of LCS
        ans = dp[n][m]

        # Construct LCS string
        result = []
        i, j = n, m
        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                result.append(s[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        result.reverse()
        return "".join(result)


obj = Solution()
r = obj.all_longest_common_subsequences("abcdef", "abc")
print(r)
