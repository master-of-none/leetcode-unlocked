"""
Binary Search
Time Complexity: O(logn)
Space Complexity: O(n)
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] < target:
                l = mid +1
            
            elif nums[mid] > target:
                r = mid - 1
            
            elif nums[mid] == target:
                return mid
        
        return -1