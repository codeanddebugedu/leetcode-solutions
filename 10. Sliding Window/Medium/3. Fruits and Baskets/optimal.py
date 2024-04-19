from typing import List

"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(1)
"""


def findMaxFruits(arr: List[int], n: int) -> int:
    fruits = {}
    n = len(arr)
    left = 0
    right = 0
    max_length = 0
    while right < n:
        fruits[arr[right]] = fruits.get(arr[right], 0) + 1
        if len(fruits) > 2:
            fruits[arr[left]] -= 1
            if fruits[arr[left]] == 0:
                del fruits[arr[left]]
            left += 1
        if len(fruits) <= 2:
            max_length = max(max_length, right - left + 1)
        right += 1
    return max_length
