from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(subset: List[int], index: int, target: int):
            if target == 0:
                result.add(tuple(subset.copy()))
                return
            elif target < 0:
                return
            if index >= len(candidates):
                return
            subset.append(candidates[index])
            target -= candidates[index]
            backtrack(subset, index + 1, target)
            subset.pop()
            target += candidates[index]
            backtrack(subset, index + 1, target)

        result = set()
        backtrack([], 0, target)
        return result


obj = Solution()

# Then convert it back to list of lists
my_list = [1, 1, 1, 2, 2]
my_list.sort()
print(obj.combinationSum2(my_list, 3))
