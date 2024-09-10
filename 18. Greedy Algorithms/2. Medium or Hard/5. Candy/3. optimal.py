from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        total = 1
        i = 1
        while i < n:
            if ratings[i] == ratings[i - 1]:
                total += 1
                i += 1
                continue
            peak = 1
            while i < n and ratings[i] > ratings[i - 1]:
                peak += 1
                total += peak
                i += 1
            down = 1
            while i < n and ratings[i] < ratings[i - 1]:
                total += down
                down += 1
                i += 1
            if down > peak:
                total += down - peak
        return total


obj = Solution()
print(obj.candy([1, 3, 5, 5, 3, 2, 1, 2, 3, 4]))
