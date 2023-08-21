import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p074_search_2D_matrix import Solution

class Testing:
    def test_search_2D_1(self):
        solution = Solution()
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        assert solution.searchMatrix(matrix, target) == True
    
    def test_search_2D_2(self):
        solution = Solution()
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        assert solution.searchMatrix(matrix, target) == False
if __name__ == "__main__":
    pytest.main()