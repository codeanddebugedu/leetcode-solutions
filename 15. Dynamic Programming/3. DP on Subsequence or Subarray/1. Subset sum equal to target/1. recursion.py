class Solution:
    def solve(self, index, target, arr):
        if target == 0:
            return True
        if index == 0:
            return arr[index] == target
        notpick = self.solve(index - 1, target, arr)
        pick = False
        if arr[index] <= target:
            pick = self.solve(index - 1, target - arr[index], arr)
        return pick or notpick

    def isSubsetSum(self, N, arr, sum):
        return self.solve(N - 1, sum, arr)
