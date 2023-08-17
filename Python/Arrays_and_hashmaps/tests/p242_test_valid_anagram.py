import os
import sys
import pytest

from p214_valid_anagram import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        s = "anagram"
        t = "nagaram"
        assert solution.isAnagram(s,t) == True
    
    def test_example_2(self):
        solution = Solution()
        s = "rat"
        t = "car"
        assert solution.isAnagram(s,t) == False

if __name__ == "__main__":
    pytest.main()

