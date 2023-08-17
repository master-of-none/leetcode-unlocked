import os
import sys
import pytest

from p238_product_of_array import Solution

class Testing:
    def test_example_1(self):
        solution = Solution()
        nums = [1,2,3,4]
        output = [24,12,8,6]
        assert solution.productExceptSelf(nums) == output
    
    def test_example_2(self):
        solution = Solution()
        nums = [-1,1,0,-3,3]
        output = [0,0,9,0,0]
        assert solution.productExceptSelf(nums) == output
        
if __name__ == "__main__":
    pytest.main()

