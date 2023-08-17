"""
Group Anagrams
Time complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[(tuple(count))].append(s)
        
        return res.values()