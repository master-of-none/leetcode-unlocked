import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p079_word_search import Solution

class Testing:
    def test_search_1(self):
        solution = Solution()
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        assert solution.exist(board, word) == True

    def test_search_2(self):
        solution = Solution()
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        assert solution.exist(board, word) == True
        
    def test_search_3(self):
        solution = Solution()
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        assert solution.exist(board, word) == False
if __name__ == "__main__":
    pytest.main()
