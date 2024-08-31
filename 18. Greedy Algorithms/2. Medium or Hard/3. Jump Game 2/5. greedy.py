from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        left = 0
        right = 0
        while right < n - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1
        return jumps
