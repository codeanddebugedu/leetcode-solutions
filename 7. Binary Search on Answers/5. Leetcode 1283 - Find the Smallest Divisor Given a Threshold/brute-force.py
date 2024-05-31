"""
The brute force approach iterates over all possible divisors from 1 to the maximum value in the nums list. Let's denote:

n as the number of elements in the nums list.
m as the maximum value in the nums list.
For each divisor, it computes the sum of the ceiling of each element divided by the divisor. This requires O(n) operations for each divisor.

Therefore, the time complexity of the brute force approach is: O(m x n)

Space Complexity = O(1)
"""

import math
from typing import List


class Solution:
    def getThreshold(self, x, nums, threshold):
        total = 0
        for num in nums:
            total += math.ceil(num / x)
        return total <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_num = max(nums)
        for divisor in range(1, max_num + 1):
            if self.getThreshold(divisor, nums, threshold):
                return divisor
        return max_num
