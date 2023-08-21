"""
Diameter of a Binary Tree
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import Optional
from tree_node import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root):
            if not root:
                return - 1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            res[0] = max(res[0], left + right +2)
            return 1 + max(left, right)

        dfs(root)
        return res[0]