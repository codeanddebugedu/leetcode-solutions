from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                if nums[i] > 2 * nums[j]:
                    count += 1
        return count
