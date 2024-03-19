"""
Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""

from sys import *
from collections import *
from math import *


def largestElement(arr: [], n: int) -> int:
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
