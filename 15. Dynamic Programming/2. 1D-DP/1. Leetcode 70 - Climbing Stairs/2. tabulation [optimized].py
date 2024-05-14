"""
Time Complexity: O(N)
Reason: We are running a simple iterative loop

Space Complexity: O(1)
Reason: We are not using any extra space.
"""


class Solution:

    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev = 1
        for i in range(2, n + 1):
            curr = prev2 + prev
            prev2 = prev
            prev = curr
        return prev
