import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p746_min_cost import Solution

class Testing:
    def test_climb_1(self):
        solution = Solution()
        cost = [10,15,20]
        assert solution.minCostClimbing(cost) == 15
    
    def test_climb_2(self):
        solution = Solution()
        cost = [1,100,1,1,1,100,1,1,100,1]
        assert solution.minCostClimbing(cost) == 6
        
        
if __name__ == "__main__":
    pytest.main()

