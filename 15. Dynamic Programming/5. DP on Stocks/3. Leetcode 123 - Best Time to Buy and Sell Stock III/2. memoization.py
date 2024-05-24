"""
Time Complexity: O(N * 2 * K), where N is the length of the prices array and 
K is the maximum number of transactions (2 in this case). 
This is due to the memoization table storing results for each state.

Space Complexity: O(N * 2 * K) + O(N), for the memoization table dp.
"""

from typing import List


class Solution:
    def solve(self, index, buy, prices, cap, dp):
        if cap == 0:
            return 0
        if index == len(prices):
            return 0
        if dp[index][buy][cap] != -1:
            return dp[index][buy][cap]
        if buy:
            buy_profit = -prices[index] + self.solve(index + 1, 0, prices, cap, dp)
            notbuy_profit = 0 + self.solve(index + 1, 1, prices, cap, dp)
            profit = max(buy_profit, notbuy_profit)
        else:
            sell_profit = prices[index] + self.solve(index + 1, 1, prices, cap - 1, dp)
            notsell_profit = 0 + self.solve(index + 1, 0, prices, cap, dp)
            profit = max(sell_profit, notsell_profit)
        dp[index][buy][cap] = profit
        return dp[index][buy][cap]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1, -1, -1] for _ in range(2)] for _ in range(n)]
        return self.solve(0, 1, prices, 2, dp)
