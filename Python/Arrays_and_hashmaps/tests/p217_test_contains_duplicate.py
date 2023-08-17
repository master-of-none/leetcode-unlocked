import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p217_contains_duplicate import Solution

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