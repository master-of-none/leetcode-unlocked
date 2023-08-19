import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p015_3Sum import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        nums = [-1,0,1,2,-1,-4]
        output = [[-1,-1,2],[-1,0,1]]
        assert solution.threeSum(nums) == output
    
    def test_example_2(self):
        solution = Solution()
        nums = [0,1,1]
        output = []
        assert solution.threeSum(nums) == output
        
    def test_example_3(self):
        solution = Solution()
        nums = [0,0,0]
        output = [[0,0,0]]
        assert solution.threeSum(nums) == output
    
if __name__ == "__main__":
    pytest.main()

