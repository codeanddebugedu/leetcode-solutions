"""
Time Complexity: O(N*2*K)
Reason: There are three nested loops that account for O(N*2*K) complexity

Space Complexity: O(K)
Reason: We are using two external arrays of size 2*K.
"""

from typing import List


class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        ahead = [[0 for _ in range(k + 1)] for _ in range(2)]
        cur = [[0 for _ in range(k + 1)] for _ in range(2)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, k + 1):
                    if buy == 0:
                        cur[buy][cap] = max(
                            0 + ahead[0][cap], -prices[ind] + ahead[1][cap]
                        )
                    elif buy == 1:
                        cur[buy][cap] = max(
                            0 + ahead[1][cap], prices[ind] + ahead[0][cap - 1]
                        )
            ahead = cur
        return ahead[0][k]
