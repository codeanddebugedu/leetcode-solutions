"""
Time complexity -> O(logN)
N is the number

Space complexity -> O(1)
"""


def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        if mid**n == m:
            return mid
        elif mid**n < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1
