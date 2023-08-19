import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p011_container_with_most_water import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        height = [1,8,6,2,5,4,8,3,7]
        output = 49
        assert solution.maxArea(height) == output
    
    def test_example_2(self):
        solution = Solution()
        height = [1,1]
        output = 1
        assert solution.maxArea(height) == output
    
if __name__ == "__main__":
    pytest.main()

