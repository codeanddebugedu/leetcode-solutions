from typing import List

"""
The worst-case time complexity can be viewed as exponential, specifically 
O(2^T) where T is the number of times we can recursively subtract the candidates 
from the target before the target reaches zero or becomes negative. 
This is because each decision point (to include or exclude a candidate) 
essentially branches the computation into two possible paths.
"""


class Solution:
    def backtrack(self, subset: List[int], index: int, target: int, candidates, result):
        if target == 0:
            result.append(subset.copy())
            return
        elif target < 0:
            return
        if index >= len(candidates):
            return
        subset.append(candidates[index])
        target -= candidates[index]
        self.backtrack(subset, index, target, candidates, result)
        subset.pop()
        target += candidates[index]
        self.backtrack(subset, index + 1, target, candidates, result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack([], 0, target, candidates, result)
        return result
