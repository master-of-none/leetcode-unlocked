import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p150_reverse_polish import Solution

class Testing:
    def test_rpn_1(self):
        solution = Solution()
        tokens = ["2","1","+","3","*"]
        assert solution.evalRPN(tokens) == 9
    
    def test_rpn_2(self):
        solution = Solution()
        tokens = ["4","13","5","/","+"]
        assert solution.evalRPN(tokens) == 6
        
    def test_rpn_3(self):
        solution = Solution()
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        assert solution.evalRPN(tokens) == 22
    

if __name__ == "__main__":
    pytest.main()

