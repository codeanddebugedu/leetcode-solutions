from sys import *
from collections import *
from math import *

"""
Time Complexity = O(n), n is number of elements in array
Space Complexity = O(1)

This code is actually similar to Brute force one
"""


def rotateArray(arr: [], n: int) -> []:
    temp = arr[0]  # storing the first element of the array in a variable
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp  # assign the value of the variable at the last index
    return arr

#Rotating using Slicing
#got "You are better than 100%" using the below
"""
def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
     
    return arr[1:] + [arr[0]]
"""