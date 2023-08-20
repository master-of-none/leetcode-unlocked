import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p543_diameter_tree import Solution

class TestSolution:
    def test_diameter_1(self):
        solution = Solution()
        input_list = [1,2,3,4,5]
        input_root = TreeNode.list_to_tree(input_list)

        actual_length = solution.diameterOfBinaryTree(input_root)

        assert actual_length == 3

    def test_diameter_2(self):
        solution = Solution()
        input_list = [1, 7]
        input_root = TreeNode.list_to_tree(input_list)

        actual_length = solution.diameterOfBinaryTree(input_root)

        assert actual_length == 1
        
if __name__ == "__main__":
    pytest.main()