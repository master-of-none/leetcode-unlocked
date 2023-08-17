import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p128_longest_consequtive_sequence import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        nums = [100,4,200,1,3,2]
        assert solution.longestConsecutive(nums) == 4
    
    def test_example_2(self):
        solution = Solution()
        nums = [0,3,7,2,5,8,4,6,0,1]
        assert solution.longestConsecutive(nums) == 9

if __name__ == "__main__":
    pytest.main()