"""
Time Complexity: O(K^N), where N is the length of the prices array, 
due to the exponential number of recursive calls.

Space Complexity: O(N), due to the recursion stack depth.
"""

from typing import List


class Solution:
    def solve(self, index, buy, prices, cap):
        if index == len(prices) or cap == 0:
            return 0
        if buy:
            buy_profit = -prices[index] + self.solve(index + 1, 0, prices, cap)
            notbuy_profit = 0 + self.solve(index + 1, 1, prices, cap)
            profit = max(buy_profit, notbuy_profit)
        else:
            sell_profit = prices[index] + self.solve(index + 1, 1, prices, cap - 1)
            notsell_profit = 0 + self.solve(index + 1, 0, prices, cap)
            profit = max(sell_profit, notsell_profit)
        return profit

    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.solve(0, 1, prices, k)
