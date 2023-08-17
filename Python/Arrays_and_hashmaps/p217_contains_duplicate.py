"""
Contains Duplicate
Using Hashset
Time Complexity - O(n)
Space Complexity - o(n)
"""
# Testing workflow
# More Testing
from typing import List
class Solution:
    """
    Solution Class
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)
        return False
