from typing import List

"""
The worst-case time complexity can be viewed as exponential, specifically 
O(2^T) where T is the number of times we can recursively subtract the candidates 
from the target before the target reaches zero or becomes negative. 
This is because each decision point (to include or exclude a candidate) 
essentially branches the computation into two possible paths.
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(subset: List[int], index: int, target: int):
            if target == 0:
                result.append(subset.copy())
                return
            elif target < 0:
                return
            if index >= len(candidates):
                return
            subset.append(candidates[index])
            target -= candidates[index]
            backtrack(subset, index, target)
            subset.pop()
            target += candidates[index]
            backtrack(subset, index + 1, target)

        result = []
        backtrack([], 0, target)
        return result
