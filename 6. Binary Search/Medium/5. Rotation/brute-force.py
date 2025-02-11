from typing import List

"""
Time complexity -> O(N)
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        for i in range(0, n - 1):
            if arr[i] > arr[i + 1]:
                return i + 1
        return 0
