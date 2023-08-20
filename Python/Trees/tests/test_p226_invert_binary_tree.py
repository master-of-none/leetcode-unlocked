import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p226_invert_binary_tree import Solution

class TestSolution:
    def test_invert_tree_1(self):
        solution = Solution()
        input_list = [4,2,7,1,3,6,9]
        expected_list = [4,7,2,9,6,3,1]

        input_root = TreeNode.list_to_tree(input_list)

        actual_root = solution.invertTree(input_root)
        actual_list = TreeNode.tree_to_list(actual_root)

        assert actual_list == expected_list
    
    def test_invert_tree_2(self):
        solution = Solution()
        input_list = [2,1,3]
        expected_list = [2,3,1]

        input_root = TreeNode.list_to_tree(input_list)

        actual_root = solution.invertTree(input_root)
        actual_list = TreeNode.tree_to_list(actual_root)

        assert actual_list == expected_list

    def test_invert_tree_3(self):
        solution = Solution()
        input_list = []
        expected_list = []

        input_root = TreeNode.list_to_tree(input_list)

        actual_root = solution.invertTree(input_root)
        actual_list = TreeNode.tree_to_list(actual_root)

        assert actual_list == expected_list

if __name__ == "__main__":
    pytest.main()