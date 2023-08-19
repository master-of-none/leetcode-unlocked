import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p020_valid_parantheses import Solution

class Testing:
    def test_parantheses_1(self):
        solution = Solution()
        s = "()"
        assert solution.isValid(s) == True
    
    def test_parantheses_2(self):
        solution = Solution()
        s = "()[]{}"
        assert solution.isValid(s) == True
        
    def test_parantheses_3(self):
        solution = Solution()
        s = "(]{"
        assert solution.isValid(s) == False
    

if __name__ == "__main__":
    pytest.main()

