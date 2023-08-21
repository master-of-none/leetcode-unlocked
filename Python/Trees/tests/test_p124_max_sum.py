import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p124_max_sum import Solution

class TestSolution:
    def test_max_sum_1(self):
        solution = Solution()
        input_list = [1, 2, 3]
        input_root = TreeNode.list_to_tree(input_list)

        actual_sum = solution.maxPathSum(input_root)

        assert actual_sum == 6
    
    def test_max_sum_2(self):
        solution = Solution()
        input_list = [-10,9,20,None,None,15,7]
        input_root = TreeNode.list_to_tree(input_list)

        actual_sum = solution.maxPathSum(input_root)

        assert actual_sum == 42
        
if __name__ == "__main__":
    pytest.main()