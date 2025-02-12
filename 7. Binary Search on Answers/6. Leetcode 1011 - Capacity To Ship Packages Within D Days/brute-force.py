from typing import List


class Solution:
    def find_days(self, weights, capacity):
        total_days = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > capacity:
                total_days += 1
                current_load = 0
            current_load += weight

        return total_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start_weight = max(weights)
        end_weight = sum(weights)
        for w in range(start_weight, end_weight + 1):
            total_days_taken = self.find_days(weights, w)
            print(w, total_days_taken)
            if total_days_taken <= days:
                # return w
                pass


obj = Solution()
obj.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
