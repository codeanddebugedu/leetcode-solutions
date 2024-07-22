"""
Time Complexity: O(N*2)
Reason: There are two nested loops that account for O(N*2) complexity

Space Complexity: O(1)

Reason: We are using an external array of size 2
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        ahead = [0, 0]  # Represents dp[ind + 1][0] and dp[ind + 1][1]
        curr = [0, 0]  # Represents dp[ind][0] and dp[ind][1]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                if buy:
                    curr[buy] = max(-prices[ind] + ahead[0], ahead[1])
                else:
                    curr[buy] = max(prices[ind] + ahead[1] - fee, ahead[0])
            ahead = curr[:]  # Move current values to ahead

        return ahead[1]  # Correct return statement
