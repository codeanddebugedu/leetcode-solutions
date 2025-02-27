from typing import List


class Solution:
    def backtrack(self, subset: List[int], index: int, target: int, result, candidates):
        if target == 0:
            result.add(tuple(subset.copy()))
            return
        elif target < 0:
            return
        if index >= len(candidates):
            return
        subset.append(candidates[index])
        target -= candidates[index]
        self.backtrack(subset, index + 1, target, result, candidates)
        subset.pop()
        target += candidates[index]
        self.backtrack(subset, index + 1, target, result, candidates)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        self.backtrack([], 0, target, result, candidates)
        return list(result)
