"""
Best Time to sell and buy stock
Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            
            else:
                l = r
        
        return maxP