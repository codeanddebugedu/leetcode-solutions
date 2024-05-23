"""
Time Complexity: O(N*2) 
Reason: There are N*2 states therefore at max 'N*2' new problems will be solved 
and we are running a for loop for 'N' times to calculate the total sum

Space Complexity: O(N*2) + O(N)
Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*2)).
"""

from typing import List


class Solution:
    def solve(self, index, buy, prices, dp):
        if index == len(prices):
            return 0
        if dp[index][buy] != -1:
            return dp[index][buy]
        if buy:
            buy_profit = -prices[index] + self.solve(index + 1, 0, prices, dp)
            notbuy_profit = 0 + self.solve(index + 1, 1, prices, dp)
            profit = max(buy_profit, notbuy_profit)
        else:
            sell_profit = prices[index] + self.solve(index + 1, 1, prices, dp)
            notsell_profit = 0 + self.solve(index + 1, 0, prices, dp)
            profit = max(sell_profit, notsell_profit)
        dp[index][buy] = profit
        return dp[index][buy]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1, -1] for _ in range(len(prices))]
        return self.solve(0, 1, prices, dp)
