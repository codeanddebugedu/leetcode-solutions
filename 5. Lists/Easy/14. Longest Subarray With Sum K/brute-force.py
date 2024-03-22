"""
Time complexity -> O(n^3)
n is number of elements in nums

Space complexity -> O(1)
"""


def longestSubarrayWithSumK(nums: [int], k: int) -> int:
    n = len(nums)

    length = 0
    for i in range(n):
        for j in range(i, n):
            s = 0
            for K in range(i, j + 1):
                s += nums[K]
            if s == k:
                length = max(length, j - i + 1)
    return length
