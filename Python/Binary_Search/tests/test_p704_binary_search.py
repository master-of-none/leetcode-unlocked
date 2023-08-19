import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p704_binary_search import Solution

class Testing:
    def test_bs_1(self):
        solution = Solution()
        nums = [-1,0,3,5,9,12]
        target = 9
        assert solution.search(nums, target) == 4
    
    def test_bs_2(self):
        solution = Solution()
        nums = [-1,0,3,5,9,12]
        target = 2
        assert solution.search(nums, target) == -1

if __name__ == "__main__":
    pytest.main()