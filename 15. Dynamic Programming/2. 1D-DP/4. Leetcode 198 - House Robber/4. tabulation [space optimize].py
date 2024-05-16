"""
Time Complexity: O(N)
Reason: We are running a simple iterative loop

Space Complexity: O(1)
"""

from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
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
