import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tree_node import TreeNode
from p235_lca import Solution

class TestSolution:
    def test_lca_1(self):
        solution = Solution()
        
        root = [6,2,8,0,4,7,9,None,None,3,5]
        p = [2]
        q = [8]
        
        p_root = TreeNode.list_to_tree(p)
        q_root = TreeNode.list_to_tree(q)
        
        root = TreeNode.list_to_tree(root)
        
        head_val = solution.lowestCommonAncestor(root, p_root, q_root)
        actual_head = TreeNode.tree_to_list(head_val)
        assert actual_head[0] == 6

    def test_lca_2(self):
        solution = Solution()
        
        root = [6,2,8,0,4,7,9,None,None,3,5]
        p = [2]
        q = [4]
        
        p_root = TreeNode.list_to_tree(p)
        q_root = TreeNode.list_to_tree(q)
        
        root = TreeNode.list_to_tree(root)
        
        head_val = solution.lowestCommonAncestor(root, p_root, q_root)
        actual_head = TreeNode.tree_to_list(head_val)
        assert actual_head[0] == 2
    
    def test_lca_3(self):
        solution = Solution()
        
        root = [2, 1]
        p = [2]
        q = [1]
        
        p_root = TreeNode.list_to_tree(p)
        q_root = TreeNode.list_to_tree(q)
        
        root = TreeNode.list_to_tree(root)
        
        head_val = solution.lowestCommonAncestor(root, p_root, q_root)
        actual_head = TreeNode.tree_to_list(head_val)
        assert actual_head[0] == 1
if __name__ == "__main__":
    pytest.main()