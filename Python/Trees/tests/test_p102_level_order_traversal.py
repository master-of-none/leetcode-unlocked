import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p102_level_order_traversal import Solution

class TestSolution:
    def test_traversal_1(self):
        solution = Solution()
        
        root_list = [3,9,20,None,None,15,7]
        
        root = TreeNode.list_to_tree(root_list)
        actual_output = solution.levelOrder(root)
        expected_output = [[3],[9,20],[15,7]]
        
        assert actual_output == expected_output
    
    def test_traversal_2(self):
        solution = Solution()
        
        root_list = [3]
        
        root = TreeNode.list_to_tree(root_list)
        actual_output = solution.levelOrder(root)
        expected_output = [[3]]
        
        assert actual_output == expected_output
        
    def test_traversal_3(self):
        solution = Solution()
        
        root_list = []
        
        root = TreeNode.list_to_tree(root_list)
        actual_output = solution.levelOrder(root)
        expected_output = []
        
        assert actual_output == expected_output
if __name__ == "__main__":
    pytest.main()