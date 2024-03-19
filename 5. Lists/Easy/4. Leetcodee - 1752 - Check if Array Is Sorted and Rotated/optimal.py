from typing import List

"""
Time complexity = O(N) where N is the number of elements in list
Because we looping through the array only once

Space complexity = O(1)
"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # We will count the rotations, we know the array can rotated only 1 time
        # and can be sorted, if the rotation will be greater than 1, we know the
        # array is not sorted and this return false
        rotations = 0
        for i in range(0, len(nums)):
            if nums[i] > nums[(i + 1) % n]:
                rotations += 1
            if rotations > 1:
                return False
        return True
