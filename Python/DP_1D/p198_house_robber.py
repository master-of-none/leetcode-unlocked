"""
House Robber
"""
from typing import List
class Solution:
    def houseRobber(self, nums: List[int]):
        rob1 = 0
        rob2 = 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2