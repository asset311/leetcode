'''
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
'''
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        # needs to have at least 2 prices and more than 0 buys/sells
        if len(prices) < 2 or k<1:
            return 0
        
        # if k is larger than the upper bound on buys and sells we can do
        # then we can just keep buying at selling at each possible opportunity
        n = len(prices)
        if k > n//2:
            profit = 0
            for i in range(1,n):
                profit += max(0, prices[i] - prices[i-1])
            return profit
        
        # else we generalize the case of first_buy -> first_sell -> ...
        buy = [-float('inf')]*k
        sell = [0]*k
        
        for i in range(n):
            for j in range(k):
                buy[j] = max(buy[j], (sell[j-1] if j>0 else 0) - prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])
        
        return sell[-1]