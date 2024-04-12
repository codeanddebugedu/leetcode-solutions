"""
Time complexity -> O(logN)
N is the number

Space complexity -> O(1)
"""


def floorSqrt(n):
    low = 0
    high = n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return high


n = int(input())
print(floorSqrt(n))
