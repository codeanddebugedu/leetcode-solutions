from typing import List

"""
Time complexity -> O(logN)
Here, N = size of the given array.

Space complexity -> O(1)
"""


def findKRotation(nums: List[int]) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    minimum = float("inf")
    index = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[low] <= nums[high]:
            if nums[low] < minimum:
                minimum = nums[low]
                index = low
            break
        if nums[low] <= nums[mid]:
            if nums[low] < minimum:
                minimum = nums[low]
                index = low
            low = mid + 1
        else:
            if nums[mid] < minimum:
                minimum = nums[mid]
                index = mid
            high = mid - 1
    return index
