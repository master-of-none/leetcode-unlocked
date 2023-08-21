import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p104_max_depth_tree import Solution

class TestSolution:
    def test_max_depth_1(self):
        solution = Solution()
        input_list = [3,9,20,None,None,15,7]
        input_root = TreeNode.list_to_tree(input_list)

        actual_depth = solution.maxDepth(input_root)

        assert actual_depth == 3

    def test_max_depth_2(self):
        solution = Solution()
        input_list = [1,None,7]
        input_root = TreeNode.list_to_tree(input_list)

        actual_depth = solution.maxDepth(input_root)

        assert actual_depth == 2
        
if __name__ == "__main__":
    pytest.main()