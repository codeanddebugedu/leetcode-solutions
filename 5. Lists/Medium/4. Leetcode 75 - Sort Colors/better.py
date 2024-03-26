from typing import List

"""
Time complexity -> O(2N) -> O(N)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        for i in range(0, n):
            if nums[i] == 0:
                cnt1 += 1
            elif nums[i] == 1:
                cnt2 += 1
            else:
                cnt3 += 1
        for i in range(0, cnt1):
            nums[i] = 0
        for i in range(cnt1, cnt1 + cnt2):
            nums[i] = 1
        for i in range(cnt1 + cnt2, cnt1 + cnt2 + cnt3):
            nums[i] = 2
