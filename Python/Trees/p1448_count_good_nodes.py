"""
Count the good nodes
DFS
"""

from typing import Optional
from tree_node import TreeNode

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, maxVal):
            if not root:
                return 0
            
            res = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)
            
            return res
        
        return dfs(root, root.val)