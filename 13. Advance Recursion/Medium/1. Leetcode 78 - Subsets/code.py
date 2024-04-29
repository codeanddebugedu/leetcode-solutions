from typing import List

"""
Time Complexity: O(2^n)

Space Complexity: O(n) -> recursion stack
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(subset, idx):
            if idx >= len(nums):
                ans.append(subset[:])
                return
            subset.append(nums[idx])
            backtrack(subset, idx + 1)
            subset.pop()
            backtrack(subset, idx + 1)

        backtrack([], 0)
        return ans
