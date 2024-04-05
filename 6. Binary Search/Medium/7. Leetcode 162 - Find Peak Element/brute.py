from typing import List

"""
Time complexity -> O(N)
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n):
            if (i == 0 or arr[i - 1] < arr[i]) and (i == n - 1 or arr[i] > arr[i + 1]):
                return i
