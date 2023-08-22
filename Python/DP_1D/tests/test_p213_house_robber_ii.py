import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p213_house_robber_ii import Solution

class Testing:
    def test_rob_1(self):
        solution = Solution()
        nums = [2,3,2]
        assert solution.rob(nums) == 3
    
    def test_rob_2(self):
        solution = Solution()
        nums = [1,2,3,1]
        assert solution.rob(nums) == 4
        
    def test_rob_3(self):
        solution = Solution()
        nums = [1,2,3]
        assert solution.rob(nums) == 3
        
if __name__ == "__main__":
    pytest.main()
    
