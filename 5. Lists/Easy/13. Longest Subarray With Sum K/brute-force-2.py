"""
Time complexity -> O(n^2)
n is number of elements in nums

Space complexity -> O(1)
"""


# Part 2
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    n = len(a)

    length = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s == k:
                length = max(length, j - i + 1)
    return length
