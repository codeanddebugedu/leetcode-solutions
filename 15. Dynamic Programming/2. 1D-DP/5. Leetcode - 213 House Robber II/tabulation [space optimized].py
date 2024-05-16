"""
Time Complexity: O(N)
Reason: We are running a simple iterative loop, two times. 
Therefore total time complexity will be O(N) + O(N) ≈ O(N)

Space Complexity: O(1)
Reason: We are not using extra space.
"""

from typing import List


class Solution:

    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev = nums[0]
        for index in range(1, n):
            pick = nums[index]
            if index > 1:
                pick += prev2
            notpick = 0 + prev
            curr = max(pick, notpick)
            prev2 = prev
            prev = curr
        return prev

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.solve(nums[1:]), self.solve(nums[:-1]))
