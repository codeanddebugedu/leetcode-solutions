from sys import *
from collections import *
from math import *

"""
Time Complexity = O(n), n is number of elements in array
Space Complexity = O(1)
"""


def rotateArray(arr: [], n: int) -> []:
    last_element = arr.pop(0)
    arr.append(last_element)
    return arr
