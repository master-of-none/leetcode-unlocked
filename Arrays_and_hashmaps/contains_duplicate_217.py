"""
Contains Duplicate
Using Hashset
Time Complexity - O(n)
Space Complexity - o(n)
"""
from typing import List
import pytest

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

class Testing:
    def test_example_1(self):
        solution = Solution()
        nums = [1, 2, 3, 1]
        assert solution.containsDuplicate(nums) == True
    
    def test_example_2(self):
        solution = Solution()
        nums = [1,2,3,4]
        assert solution.containsDuplicate(nums) == False
    
    def test_example_3(self):
        solution = Solution()
        nums = [1,1,1,3,3,4,3,2,4,2]
        assert solution.containsDuplicate(nums) == True

if __name__ == "__main__":
    pytest.main()