"""
Time Complexity: O(N * 2 * K), where N is the length of the prices array and 
K is the maximum number of transactions (2 in this case). 
This is due to the memoization table storing results for each state.

Space Complexity: O(N * 2 * K), for the memoization table dp.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1, -1, -1] for _ in range(2)] for _ in range(n + 1)]
        for ind in range(n + 1):
            for buy in range(2):
                dp[ind][buy][0] = 0
        for buy in range(2):
            for cap in range(3):
                dp[n][buy][cap] = 0
        for ind in range(n - 1, -1, -1):
            for buy in range(0, 2):
                for cap in range(1, 3):
                    profit = 0
                    if buy:
                        buy_profit = -prices[ind] + dp[ind + 1][0][cap]
                        not_buy_profit = 0 + dp[ind + 1][1][cap]
                        profit = max(buy_profit, not_buy_profit)
                    else:
                        sell_profit = prices[ind] + dp[ind + 1][1][cap - 1]
                        not_sell_profit = 0 + dp[ind + 1][0][cap]
                        profit = max(sell_profit, not_sell_profit)
                    dp[ind][buy][cap] = profit
        return dp[0][1][2]
