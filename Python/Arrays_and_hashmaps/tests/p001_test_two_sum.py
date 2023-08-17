import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p001_two_sum import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        assert solution.twoSum(nums, target) == [0, 1]
    
    def test_example_2(self):
        solution = Solution()
        nums = [3, 2, 4]
        target = 6
        assert solution.twoSum(nums, target) == [1, 2]
    
    def test_example_3(self):
        solution = Solution()
        nums = [3, 3]
        target = 6
        assert solution.twoSum(nums, target) == [0, 1]

if __name__ == "__main__":
    pytest.main()
