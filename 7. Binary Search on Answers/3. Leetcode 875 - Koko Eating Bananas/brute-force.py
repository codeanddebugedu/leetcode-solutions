import math
from typing import List

"""
Time complexity -> O(N * max(piles))
N is the number

Space complexity -> O(1)
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalHours(piles, hourly_rate):
            total = 0
            for i in range(len(piles)):
                total = total + math.ceil(piles[i] / hourly_rate)
            return total

        maximum_banana = max(piles)
        for i in range(1, maximum_banana + 1):
            total_hour = totalHours(piles, i)
            if total_hour <= h:
                return i
