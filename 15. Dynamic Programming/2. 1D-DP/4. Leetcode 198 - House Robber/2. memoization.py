"""
Time Complexity: O(N)
Reason: The overlapping subproblems will return the answer in constant time O(1). 
Therefore the total number of new subproblems we solve is 'n'. 
Hence total time complexity is O(N).

Space Complexity: O(N)
Reason: We are using a recursion stack space(O(N)) and an array (again O(N)). 
Therefore total space complexity will be O(N) + O(N) ≈ O(N)
"""

from typing import List


class Solution:
    def solve(self, index, nums, dp):
        if index == 0:
            return nums[index]
        if index == -1:
            return 0
        if dp[index] != -1:
            return dp[index]
        pick = nums[index] + self.solve(index - 2, nums, dp)
        notpick = 0 + self.solve(index - 1, nums, dp)
        dp[index] = max(pick, notpick)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        return self.solve(n - 1, nums, dp)
