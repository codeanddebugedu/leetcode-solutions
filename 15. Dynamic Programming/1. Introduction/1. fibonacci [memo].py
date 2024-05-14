"""
Time complexity -> O(N)
Space complexity -> O(N) + O(N)
"""


def fibonacci(num, dp):
    if num <= 1:
        return num
    if dp[num] != -1:
        return dp[num]
    dp[num] = fibonacci(num - 1, dp) + fibonacci(num - 2, dp)
    return dp[num]


if __name__ == "__main__":
    n = 5
    dp = [-1] * (n + 1)
    print(fibonacci(n, dp))
