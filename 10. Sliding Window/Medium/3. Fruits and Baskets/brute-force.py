from typing import List

"""
Time complexity -> O(N^2)
N is the number of elements in arr

Space complexity -> O(3)
"""


def findMaxFruits(arr: List[int], n: int) -> int:
    n = len(arr)
    max_length = 0
    for i in range(n):
        fruits = set()
        for j in range(i, n):
            fruits.add(arr[j])
            if len(fruits) > 2:
                break
            max_length = max(max_length, j - i + 1)
    return max_length
