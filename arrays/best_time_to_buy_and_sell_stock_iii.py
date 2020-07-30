'''
123. Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # sequence if first_buy -> first_sell -> second_buy -> second_sell
        first_buy, first_sell = -float('inf'), 0
        second_buy, second_sell = -float('inf'), 0
        
        for price in prices:
            first_buy = max(first_buy, -price) # buying low
            first_sell = max(first_sell, first_buy + price) # maximizing first profit
            second_buy = max(second_buy, first_sell - price) # buying at next low
            second_sell = max(second_sell, second_buy + price) # maximizing second profit
        
        return second_sell
