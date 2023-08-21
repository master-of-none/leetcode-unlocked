"""
Tree in Python
Function to add to tree and get from tree
"""

class TreeNode:
    def __init__(self, val = None, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_to_tree(node):
        if not node:
            return None
        
        root = TreeNode(node[0]) if node[0] is not None else None
        queue = [root] if root else []
        i = 1
        
        while queue and i < len(node):
            cur = queue.pop(0)
            
            if cur:
                if node[i] is not None:
                    cur.left = TreeNode(node[i])
                    queue.append(cur.left)
                else:
                    queue.append(None)
                
                i += 1
                
                if i < len(node) and node[i] is not None:
                    cur.right = TreeNode(node[i])
                    queue.append(cur.right)
                
                else:
                    queue.append(None)
                
                i += 1
                
            else:
                i += 2
                
        return root
    
    @staticmethod
    def tree_to_list(root):
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            cur = queue.pop(0)
            # result.append(cur.val if cur else None)
            
            if cur:
                result.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
        
        return result