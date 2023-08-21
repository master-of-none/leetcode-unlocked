import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p105_tree_preorder_inorder import Solution

class TestSolution:
    def test_pre_in_1(self):
        solution = Solution()
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]

        actual_head = solution.buildTree(preorder, inorder)
        
        actual_list = TreeNode.tree_to_list(actual_head)
        output = [3,9,20,15,7]
        assert actual_list == output
    
    def test_pre_in_2(self):
        solution = Solution()
        preorder = [-1]
        inorder = [-1]

        actual_head = solution.buildTree(preorder, inorder)
        
        actual_list = TreeNode.tree_to_list(actual_head)
        output = [-1]
        assert actual_list == output
        
if __name__ == "__main__":
    pytest.main()