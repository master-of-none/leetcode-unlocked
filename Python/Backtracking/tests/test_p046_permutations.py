import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p046_permutations import Solution

class Testing:
    def test_permutations_1(self):
        solution = Solution()
        nums = [1, 2, 3]
        output = [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
        assert solution.permute(nums) == output
    
    def test_permutations_2(self):
        solution = Solution()
        nums = [1, 2]
        output = [[2, 1], [1, 2]]
        assert solution.permute(nums) == output
    
    def test_permutations_3(self):
        solution = Solution()
        nums = [1]
        output = [[1]]
        assert solution.permute(nums) == output

if __name__ == "__main__":
    pytest.main()
