"""
Lowest Common Ancestor of BST
"""

from typing import Optional
from tree_node import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            else:
                return cur
            
                