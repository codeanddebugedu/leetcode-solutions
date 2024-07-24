"""
Time complexity - O(n^2)
Space complexity - O(1)
"""


class Solution:
    def maxLen(self, n, arr):
        max_length = 0
        n = len(arr)
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += arr[j]
                if sum == 0:
                    max_length = max(max_length, j - i + 1)
        return max_length
