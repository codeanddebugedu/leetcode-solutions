"""
Time complexity -> O(N)
Space complexity -> O(N)
"""

n = 6
dp = [-1] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
