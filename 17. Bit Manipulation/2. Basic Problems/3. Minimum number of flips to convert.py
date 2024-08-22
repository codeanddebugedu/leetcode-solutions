# Optimal 1
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        count = 0
        for i in range(0, 32):
            if ans & (1 << i) != 0:
                count += 1
        return count


# Optimal 2
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        count = 0
        while ans > 0:
            if ans % 2 == 1:
                count += 1
            ans = ans // 2
        return count
