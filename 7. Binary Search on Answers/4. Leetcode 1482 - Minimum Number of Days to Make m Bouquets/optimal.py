from typing import List


class Solution:
    def canMakeBouquet(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        total = 0
        count = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                count += 1
                if count == k:
                    total += 1
                    count = 0
            else:
                count = 0
        return total >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        low, high = min(bloomDay), max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if self.canMakeBouquet(bloomDay, m, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
