import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p199_right_side_view import Solution

class TestSolution:
    def test_right_side_1(self):
        solution = Solution()
        
        root_list = [1,2,3,None,5,None,4]
        
        root = TreeNode.list_to_tree(root_list)
        actual_output = solution.rightSideView(root)
        expected_output = [1, 3, 4]
        
        assert actual_output == expected_output
    
    def test_right_side_2(self):
        solution = Solution()
        
        root_list = [1,None,3]
        
        root = TreeNode.list_to_tree(root_list)
        actual_output = solution.rightSideView(root)
        expected_output = [1, 3]
        
        assert actual_output == expected_output
    
    def test_right_side_3(self):
        solution = Solution()
        
        root_list = []
        
        root = TreeNode.list_to_tree(root_list)
        actual_output = solution.rightSideView(root)
        expected_output = []
        
        assert actual_output == expected_output
    
if __name__ == "__main__":
    pytest.main()