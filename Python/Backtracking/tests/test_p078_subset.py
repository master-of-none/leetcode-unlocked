import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p078_subset import Solution

class Testing:
    def test_subset_1(self):
        solution = Solution()
        nums = [1, 2, 3]
        output = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
        assert solution.subsets(nums) == output

    def test_subset_2(self):
        solution = Solution()
        nums = [0]
        output = [[0], []]
        assert solution.subsets(nums) == output
if __name__ == "__main__":
    pytest.main()
