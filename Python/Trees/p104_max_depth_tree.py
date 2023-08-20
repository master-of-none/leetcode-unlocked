"""
Max Depth of Binary Tree
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional
from tree_node import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))