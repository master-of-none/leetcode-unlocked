import os
import sys
import pytest

from p347_top_k_frequent_elements import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        nums = [1,1,1,2,2,3]
        k = 2
        assert solution.topKFrequent(nums,k) == [1, 2]
    
    def test_example_2(self):
        solution = Solution()
        nums = [1]
        k = 1
        assert solution.topKFrequent(nums,k) == [1]
if __name__ == "__main__":
    pytest.main()

