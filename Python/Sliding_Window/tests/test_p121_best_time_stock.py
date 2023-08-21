import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p121_best_time_stock import Solution

class Testing:
    def test_stock_1(self):
        solution = Solution()
        prices = [7,1,5,3,6,4]
        assert solution.maxProfit(prices) == 5
    
    def test_stock_2(self):
        solution = Solution()
        prices = [7,6,4,3,1]
        assert solution.maxProfit(prices) == 0
if __name__ == "__main__":
    pytest.main()