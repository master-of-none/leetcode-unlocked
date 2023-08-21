"""
Subtree of another Tree
"""

from typing import Optional
from tree_node import TreeNode

class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        
        if not t:
            return True
        
        if not s:
            return False
        
        if self.isSameTree(s, t):
            return True
        
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
    
    def isSameTree(self, s, t):
        if not s and not t:
            return True
            
        if s and t and s.val == t.val:
            return (self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right))
        
        return False