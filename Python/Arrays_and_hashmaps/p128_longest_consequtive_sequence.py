"""
Longest Consequitve Sequence
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        
        for n in nums:
            if (n - 1) not in hashset:
                length = 0
                
                while (n+length) in hashset:
                    length += 1
                
                res = max(length, res)

        return res
        