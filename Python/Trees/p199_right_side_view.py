"""
Right Side View of Tree
BFS Approach
"""

from typing import Optional, List
from tree_node import TreeNode
import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            temp = None
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    temp = node
                    q.append(node.left)
                    q.append(node.right)
                
            if temp:
                res.append(temp.val)
        
        return res
        