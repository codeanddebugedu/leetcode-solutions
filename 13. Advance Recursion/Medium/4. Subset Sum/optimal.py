from sys import *
from collections import *
from math import *

from typing import List


def subsetSum(num: List[int]) -> List[int]:
    def backtrack(total, index):
        if index >= len(num):
            result.append(total)
            return
        backtrack(total + num[index], index + 1)
        backtrack(total, index + 1)

    result = []
    backtrack(0, 0)
    result.sort()
    return result


print(subsetSum([1, 2, 3]))
