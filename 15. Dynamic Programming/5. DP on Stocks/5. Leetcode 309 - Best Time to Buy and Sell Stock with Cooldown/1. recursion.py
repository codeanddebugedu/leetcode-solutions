from typing import List


class Solution:
    def solve(self, index, buy, prices):
        if index >= len(prices):
            return 0
        if buy:
            buy_profit = -prices[index] + self.solve(index + 1, 0, prices)
            notbuy_profit = 0 + self.solve(index + 1, 1, prices)
            profit = max(buy_profit, notbuy_profit)
        else:
            sell_profit = prices[index] + self.solve(index + 2, 1, prices)
            notsell_profit = 0 + self.solve(index + 1, 0, prices)
            profit = max(sell_profit, notsell_profit)
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(0, 1, prices)
