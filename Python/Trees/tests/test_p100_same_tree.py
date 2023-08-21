import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p100_same_tree import Solution

class TestSolution:
    def test_same_tree_1(self):
        solution = Solution()
        
        p = [1, 2, 3]
        q = [1, 2, 3]
        
        p_head = TreeNode.list_to_tree(p)
        q_head = TreeNode.list_to_tree(q)
        
        assert solution.isSameTree(p_head, q_head) == True

    def test_same_tree_2(self):
        solution = Solution()
        
        p = [1, 2, 1]
        q = [1, 1, 2]
        
        p_head = TreeNode.list_to_tree(p)
        q_head = TreeNode.list_to_tree(q)
        
        assert solution.isSameTree(p_head, q_head) == False
    
    def test_same_tree_3(self):
        solution = Solution()
       
        p = [1, 2]
        q = [1, None, 2]
        
        p_head = TreeNode.list_to_tree(p)
        q_head = TreeNode.list_to_tree(q)
        
        assert solution.isSameTree(p_head, q_head) == False

if __name__ == "__main__":
    pytest.main()