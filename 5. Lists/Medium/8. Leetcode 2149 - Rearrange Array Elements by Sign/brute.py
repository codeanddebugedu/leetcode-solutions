from typing import List

"""
Time complexity -> O(N+N/2)
N is number of elements in nums

Space complexity -> O(N/2 + N/2)
"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        for i in range(len(pos)):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]

        return nums
