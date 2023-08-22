import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p198_house_robber import Solution

class Testing:
    def test_rob_1(self):
        solution = Solution()
        nums = [1,2,3,1]
        assert solution.houseRobber(nums) == 4
    
    def test_rob_2(self):
        solution = Solution()
        nums = [2,7,9,3,1]
        assert solution.houseRobber(nums) == 12
        
        
if __name__ == "__main__":
    pytest.main()

