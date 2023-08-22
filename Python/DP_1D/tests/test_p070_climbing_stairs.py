import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p070_climbing_stairs import Solution

class Testing:
    def test_stairs_1(self):
        solution = Solution()
        n = 2
        assert solution.climbStairs(n) == 2
    
    def test_stairs_2(self):
        solution = Solution()
        n = 3
        assert solution.climbStairs(n) == 3
        
    def test_stairs_3(self):
        solution = Solution()
        n = 10
        assert solution.climbStairs(n) == 89
        
if __name__ == "__main__":
    pytest.main()

