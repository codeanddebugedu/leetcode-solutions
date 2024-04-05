from typing import List

"""
Time complexity -> O(logN)
Here, N = size of the given array.

Space complexity -> O(1)
"""


class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if low == high:
                return arr[low]
            if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
                return arr[mid]
            if arr[mid] == arr[mid - 1]:
                if mid % 2 == 1:
                    low = mid + 1
                else:
                    high = mid - 1
            elif arr[mid] == arr[mid + 1]:
                if mid % 2 == 1:
                    high = mid - 1
                else:
                    low = mid + 1
