import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p051_n_queens import Solution

class Testing:
    def test_queen_1(self):
        solution = Solution()
        n = 4
        output = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        assert solution.solveNQueens(n) == output

    def test_queen_2(self):
        solution = Solution()
        n = 1
        output = [["Q"]]
        assert solution.solveNQueens(n) == output
    
if __name__ == "__main__":
    pytest.main()
