import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p110_balanced_binary_tree import Solution

class TestSolution:
    def test_balanced_1(self):
        solution = Solution()
        input_list = [3,9,20,None,None,15,7]
        input_root = TreeNode.list_to_tree(input_list)
        
        assert solution.isBalanced(input_root) == True

    def test_balanced_2(self):
        solution = Solution()
        input_list = [1,2,2,3,3,None,None,4,4]
        input_root = TreeNode.list_to_tree(input_list)
        
        assert solution.isBalanced(input_root) == False
    
    def test_balanced_3(self):
        solution = Solution()
        input_list = []
        input_root = TreeNode.list_to_tree(input_list)
        
        assert solution.isBalanced(input_root) == True

if __name__ == "__main__":
    pytest.main()