import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p022_generate_parantheses import Solution

class Testing:
    def test_generate_1(self):
        solution = Solution()
        n = 3
        output = ["((()))","(()())","(())()","()(())","()()()"]
        assert solution.generateParenthesis(n) == output

    def test_generate_1(self):
        solution = Solution()
        n = 1
        output = ["()"]
        assert solution.generateParenthesis(n) == output
    