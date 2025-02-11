"""
Time Complexity:
The binary search algorithm runs in O(log m) time, where m is the maximum value in the nums list. 
For each iteration of the binary search, the getThreshold function is called, which runs in O(n) time, 
where n is the number of elements in the nums list. 
Therefore, the overall time complexity is O(n log m).

Space Complexity:
The space complexity of this code is O(1) because it uses a constant amount of extra 
space regardless of the input size.
"""

import math
from typing import List


class Solution:
    def calTotal(self, nums, n):
        total = 0
        for num in nums:
            total = total + math.ceil(num / n)
        return total

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maxi = max(nums)
        low = 1
        high = maxi
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            total = self.calTotal(nums, mid)
            if total <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
