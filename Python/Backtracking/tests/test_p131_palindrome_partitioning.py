import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p131_palindrome_partitioning import Solution

class Testing:
    def test_palindrome_1(self):
        solution = Solution()
        s = "aab"
        output = [["a","a","b"],["aa","b"]]
        assert solution.partition(s) == output

    def test_palindrome_2(self):
        solution = Solution()
        s = "a"
        output = [["a"]]
        assert solution.partition(s) == output
    
if __name__ == "__main__":
    pytest.main()
