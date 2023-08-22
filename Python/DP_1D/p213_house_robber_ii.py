"""
House Robber II
"""
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.houseRob(nums[1:]), self.houseRob(nums[:-1]))
    
    def houseRob(self, nums):
        rob1 = 0
        rob2 = 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

