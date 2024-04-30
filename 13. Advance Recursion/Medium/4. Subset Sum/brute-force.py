from sys import *
from collections import *
from math import *

from typing import List


def subsetSum(num: List[int]) -> List[int]:
    def backtrack(subset, index):
        if index >= len(num):
            result.append(sum(subset))
            return
        subset.append(num[index])
        backtrack(subset, index + 1)
        subset.pop()
        backtrack(subset, index + 1)

    result = []
    backtrack([], 0)
    result.sort()
    return result
