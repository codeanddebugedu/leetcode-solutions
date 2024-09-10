from typing import List


class Solution:
    def findDays(self, weights, cap):
        days = 1
        load = 0
        n = len(weights)

        for i in range(n):
            load += weights[i]
            if load > cap:
                days += 1
                load = weights[i]  # Start a new day with the current weight
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
