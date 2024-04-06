"""
Time complexity -> O(N)
N is the number

Space complexity -> O(1)
"""


def NthRoot(n: int, m: int) -> int:
    for i in range(1, m + 1):
        if i**n == m:
            return i
    return -1
