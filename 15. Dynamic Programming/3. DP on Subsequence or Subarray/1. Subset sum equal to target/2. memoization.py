class Solution:
    def solve(self, index, target, arr, dp):
        if target == 0:
            return True
        if index == 0:
            return arr[index] == target
        if dp[index][target] != -1:
            return dp[index][target]
        notpick = self.solve(index - 1, target, arr, dp)
        pick = False
        if arr[index] <= target:
            pick = self.solve(index - 1, target - arr[index], arr, dp)
        dp[index][target] = pick or notpick
        return dp[index][target]

    def isSubsetSum(self, N, arr, sum):
        dp = [[-1 for _ in range(sum + 1)] for _ in range(N)]
        return self.solve(N - 1, sum, arr, dp)
