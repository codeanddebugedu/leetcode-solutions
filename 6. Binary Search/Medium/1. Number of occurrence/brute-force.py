"""
Time complexity -> O(N)
N is number of elements in nums

Space complexity -> O(1)
"""


def count(arr: [int], n: int, target: int) -> int:
    cnt = 0
    for i in range(n):
        if arr[i] == target:
            cnt += 1
    return cnt
