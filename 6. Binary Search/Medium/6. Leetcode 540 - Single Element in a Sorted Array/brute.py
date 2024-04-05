from typing import List

"""
Time complexity -> O(N)
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        for i in range(n):
            if i == 0:
                if arr[i] != arr[i + 1]:
                    return arr[i]
            elif i == n - 1:
                if arr[i] != arr[i - 1]:
                    return arr[i]
            else:
                if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                    return arr[i]
