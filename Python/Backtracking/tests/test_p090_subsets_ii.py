import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p090_subsets_ii import Solution

class Testing:
    def test_subset_wdups_1(self):
        solution = Solution()
        nums = [1, 2, 2]
        output = [[1, 2, 2], [1, 2], [1], [2, 2], [2], []]
        assert solution.subsetsWithoutDup(nums) == output
    
    def test_subset_wdups_2(self):
        solution = Solution()
        nums = [1]
        output = [[1], []]
        assert solution.subsetsWithoutDup(nums) == output

if __name__ == "__main__":
    pytest.main()
