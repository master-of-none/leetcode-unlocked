import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from two_sum_II_sorted import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        numbers = [2, 7, 11, 15]
        target = 9
        assert solution.twoSum(numbers, target) == [1, 2]
    
    def test_example_2(self):
        solution = Solution()
        numbers = [2, 3, 4]
        target = 6
        assert solution.twoSum(numbers, target) == [1, 3]

if __name__ == "__main__":
    pytest.main()

