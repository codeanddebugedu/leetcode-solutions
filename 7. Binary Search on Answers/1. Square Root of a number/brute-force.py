"""
Time complexity -> O(N)
N is the number

Space complexity -> O(1)
"""


def floorSqrt(n):
    ans = 0
    for i in range(0, n + 1):
        if i * i <= n:
            ans = i
        else:
            break
    return ans


n = int(input())
print(floorSqrt(n))
