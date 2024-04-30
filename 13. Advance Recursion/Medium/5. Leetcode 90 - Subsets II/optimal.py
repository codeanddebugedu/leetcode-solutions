from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subset, index):
            result.append(subset.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()

        result = []
        nums.sort()
        backtrack([], 0)
        return result
