'''
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if we think of peaks and valleys, we can see
        # we can see that we can just buy and sell whenever the next price is higher
        
        profit = 0
        
        if len(prices) < 2:
            return 0
        
        for i in range(1,len(prices)):
            profit += max(prices[i] - prices[i-1], 0)
        
        return profit