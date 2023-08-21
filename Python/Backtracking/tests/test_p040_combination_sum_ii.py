import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p040_combination_sum_ii import Solution

class Testing:
    def test_comb_1(self):
        solution = Solution()
        nums = [10,1,2,7,6,1,5]
        target = 8
        output = [[1,1,6], [1,2,5], [1,7], [2,6]]

        assert solution.combinationSum2(nums, target) == output

    def test_comb_2(self):
        solution = Solution()
        nums = [2,5,2,1,2]
        target = 5
        output = [[1,2,2], [5]]
        assert solution.combinationSum2(nums, target) == output
        
if __name__ == "__main__":
    pytest.main()
