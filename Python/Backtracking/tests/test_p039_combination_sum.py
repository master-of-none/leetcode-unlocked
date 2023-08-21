import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p039_combination_sum import Solution

class Testing:
    def test_combination_1(self):
        solution = Solution()
        candidates = [2,3,6,7]
        target = 7
        output = [[2,2,3],[7]]
        assert solution.combinationSum(candidates, target) == output
    
    def test_combination_2(self):
        solution = Solution()
        candidates = [2,3,5]
        target = 8
        output = [[2,2,2,2],[2,3,3],[3,5]]
        assert solution.combinationSum(candidates, target) == output
        
    def test_combination_3(self):
        solution = Solution()
        candidates = [2]
        target = 1
        output = []
        assert solution.combinationSum(candidates, target) == output

if __name__ == "__main__":
    pytest.main()
