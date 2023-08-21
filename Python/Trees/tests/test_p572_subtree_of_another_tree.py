import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p572_subtree_of_another_tree import Solution

class TestSolution:
    def test_sub_tree_1(self):
        solution = Solution()
        
        s = [3,4,5,1,2]
        t = [4,1,2]
        
        s_head = TreeNode.list_to_tree(s)
        t_head = TreeNode.list_to_tree(t)
        
        assert solution.isSubtree(s_head, t_head) == True

    def test_sub_tree_2(self):
        solution = Solution()
        
        s = [3,4,5,1,2,None,None,None,None,0]
        t = [4,1,2]
        
        s_head = TreeNode.list_to_tree(s)
        t_head = TreeNode.list_to_tree(t)
        
        assert solution.isSubtree(s_head, t_head) == False

if __name__ == "__main__":
    pytest.main()