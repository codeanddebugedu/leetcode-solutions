"""
Print all the subsequences where sum=K.
Generate every one of them

Time complexity -> O(2^n)
"""

from typing import List


def backtrack(subset: List[int], index: int, total: int):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    if index >= len(nums):
        return
    subset.append(nums[index])
    Sum = total + nums[index]
    backtrack(subset, index + 1, Sum)
    subset.pop()
    Sum = total
    backtrack(subset, index + 1, Sum)


result = []
nums = [1, 2, 3, 4, 3, 2, 1, 1, 1, 1]
k = 3
backtrack([], 0, 0)
print(result)
