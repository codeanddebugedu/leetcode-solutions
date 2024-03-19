from typing import List

"""
Time Complexity = O(N), N is length of array
Space Complexity: O(N)
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        temp = []

        # Copy non-zero elements from original to temp array
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])

        # Number of non-zero elements
        nz = len(temp)

        # Copy elements from temp to fill first nz fields of original array
        for i in range(nz):
            nums[i] = temp[i]

        # Fill the rest of the cells with 0
        for i in range(nz, n):
            nums[i] = 0
