"""
Top K Frequent Elements
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        hashmap = {}
        
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        for n, c in hashmap.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                