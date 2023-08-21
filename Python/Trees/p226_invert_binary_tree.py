"""
Invert Binary Tree
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import Optional
from tree_node import TreeNode
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
    
        return root