from typing import List

"""
Time complexity -> O(N)
N is number of elements in nums

Space complexity -> O(1)
"""


def superiorElements(arr: List[int]) -> List[int]:
    result = []
    maxi = float("-inf")
    n = len(arr)
    for i in range(n - 1, -1, -1):
        e = max(maxi, arr[i])
        if e > maxi:
            result.append(e)
            maxi = e
    return result
