import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p042_trapping_rain_water import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        output = 6
        assert solution.trap(height) == output
    
    def test_example_2(self):
        solution = Solution()
        height = [4,2,0,3,2,5]
        output = 9
        assert solution.trap(height) == output
    
if __name__ == "__main__":
    pytest.main()

