from typing import List
import math

"""
Time complexity -> O(N * log(max(piles)))

Space complexity -> O(1)
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalHours(piles, hourly_rate):
            total = 0
            for i in range(len(piles)):
                total = total + math.ceil(piles[i] / hourly_rate)
            return total

        low = 1
        high = max(piles)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            total_hours = totalHours(piles, mid)
            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
