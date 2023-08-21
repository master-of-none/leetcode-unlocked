import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p098_valid_bst import Solution

class TestSolution:
    def test_bst_1(self):
        solution = Solution()
        input_list = [2,1,3]
        input_root = TreeNode.list_to_tree(input_list)

        assert solution.isValidBST(input_root) == True
    
    def test_bst_2(self):
        solution = Solution()
        input_list = [5,1,4,None,None,3,6]
        input_root = TreeNode.list_to_tree(input_list)

        assert solution.isValidBST(input_root) == False
if __name__ == "__main__":
    pytest.main()