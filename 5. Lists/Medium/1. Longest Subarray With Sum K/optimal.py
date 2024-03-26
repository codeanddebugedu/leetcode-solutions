"""
Time complexity -> O(2N)
n is number of elements in nums

Space complexity -> O(1)
"""


def longestSubarrayWithSumK(a: [int], k: int) -> int:
    n = len(a)
    left = 0
    right = 0
    max_length = 0
    Sum = a[0]
    while right < n:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1
        if Sum == k:
            max_length = max(max_length, right - left + 1)

        right += 1
        if right < n:
            Sum += a[right]
    return max_length
