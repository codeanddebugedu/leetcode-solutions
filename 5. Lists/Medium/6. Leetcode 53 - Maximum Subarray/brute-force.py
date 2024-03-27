from typing import List

"""
Time complexity -> O(n^3)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                summ = 0

                # add all the elements of subarray
                for k in range(i, j + 1):
                    summ += nums[k]

                maxi = max(maxi, summ)
        return maxi
