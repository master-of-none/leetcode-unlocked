"""
Min cost climbing stairs
"""
from typing import List
class Solution:
    def minCostClimbing(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost)-3, -1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
        
        return min(cost[0], cost[1])