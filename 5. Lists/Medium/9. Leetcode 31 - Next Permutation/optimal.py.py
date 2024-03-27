from typing import List

"""
Time complexity -> O(3N)
N is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        ind = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        if ind == -1:
            nums.reverse()
            return nums

        # Step 2: Find the next greater element
        #         and swap it with nums[ind]:
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # Step 3: reverse the right half:
        nums[ind + 1 :] = reversed(nums[ind + 1 :])
