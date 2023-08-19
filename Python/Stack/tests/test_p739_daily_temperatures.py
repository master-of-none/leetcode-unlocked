import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from p739_daily_temperatures import Solution

class Testing:
    def test_temp_1(self):
        solution = Solution()
        temperatures = [73,74,75,71,69,72,76,73]
        output = [1,1,4,2,1,1,0,0]
        assert solution.dailyTemperatures(temperatures) == output

    def test_temp_2(self):
        solution = Solution()
        temperatures = [30,40,50,60]
        output = [1,1,1,0]
        assert solution.dailyTemperatures(temperatures) == output
        
    def test_temp_3(self):
        solution = Solution()
        temperatures = [30,60,90]
        output = [1,1,0]
        assert solution.dailyTemperatures(temperatures) == output