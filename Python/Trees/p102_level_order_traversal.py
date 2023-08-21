"""
Binary Tree level order Traversal 
Using BFS
"""

from typing import Optional, List
from tree_node import TreeNode
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
        
        return res