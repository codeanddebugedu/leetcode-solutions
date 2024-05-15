"""
Time Complexity: O(N)
Reason: We are running a simple iterative loop

Space Complexity: O(1)
Reason: We are not using any extra space.
"""


class Solution:
    def minimumEnergy(self, height, n):
        prev = 0
        prev2 = 0
        for i in range(1, n):
            jump2 = float("inf")
            jump1 = prev + abs(height[i] - height[i - 1])
            if i > 1:
                jump2 = prev2 + abs(height[i] - height[i - 2])
            cur_i = min(jump1, jump2)
            prev2 = prev
            prev = cur_i
        return prev
