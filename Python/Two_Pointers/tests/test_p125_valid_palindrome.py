import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p125_valid_palindrome import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        s = "A man, a plan, a canal: Panama"
        assert solution.isPalindrome(s) == True
    
    def test_example_2(self):
        solution = Solution()
        s = "race a car"
        assert solution.isPalindrome(s) == False
        
    def test_example_3(self):
        solution = Solution()
        s = " "
        assert solution.isPalindrome(s) == True
    
if __name__ == "__main__":
    pytest.main()

