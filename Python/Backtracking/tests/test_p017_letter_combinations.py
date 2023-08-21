import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p017_letter_combinations import Solution

class Testing:
    def test_letter_1(self):
        solution = Solution()
        digits = "23"
        output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        assert solution.letterCombinations(digits) == output

    def test_letter_2(self):
        solution = Solution()
        s = ""
        output = []
        assert solution.letterCombinations(s) == output
    
    def test_letter_3(self):
        solution = Solution()
        s = "2"
        output = ["a", "b", "c"]
        assert solution.letterCombinations(s) == output
    
if __name__ == "__main__":
    pytest.main()
