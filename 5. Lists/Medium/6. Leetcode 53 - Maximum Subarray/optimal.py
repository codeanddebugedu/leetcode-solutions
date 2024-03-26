from typing import List

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""

# Also known as Kadane’s Algorithm


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        Sum = 0
        n = len(nums)
        for i in range(n):
            Sum += nums[i]

            if Sum > maxi:
                maxi = Sum

            # If sum < 0: discard the sum calculated
            if Sum < 0:
                Sum = 0

        # To consider the sum of the empty subarray
        # uncomment the following check:

        # if maxi < 0: maxi = 0

        return maxi
