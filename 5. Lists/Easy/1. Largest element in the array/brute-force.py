"""
Time complexity = O(N logN) where N is the number of elements in list
Space complexity = O(1)
"""

from sys import *
from collections import *
from math import *


def largestElement(arr: [], n: int) -> int:
    # Sort the elements first
    arr.sort()

    # Return the largest from the end
    return arr[-1]
