from typing import List


class Solution:
    def findDays(self, weights, cap):
        days = 1
        load = 0
        n = len(weights)
        for i in range(n):
            if load + weights[i] > cap:
                days += 1
                load = weights[i]
            else:
                load += weights[i]
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Do the below calculation using FOR loop
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            numberOfDays = self.findDays(weights, mid)
            if numberOfDays <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
