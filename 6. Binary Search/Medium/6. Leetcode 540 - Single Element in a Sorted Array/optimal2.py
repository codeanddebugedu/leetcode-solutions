from typing import List

"""
Time complexity -> O(logN)
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
                return arr[mid]
            elif (arr[mid] == arr[mid - 1] and mid % 2 == 1) or (
                arr[mid] == arr[mid + 1] and mid % 2 == 0
            ):
                low = mid + 1
            else:
                high = mid - 1
