from typing import List

"""
Time complexity -> O(n^2)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        n = len(nums)
        for i in range(n):
            sum = 0
            for j in range(i, n):

                # add the current element arr[j]
                # to the sum i.e. sum of arr[i...j-1]
                sum += nums[j]

                maxi = max(maxi, sum)  # getting the maximum
        return maxi
