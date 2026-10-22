# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(q, p):
            if not q and not p:
                return True
            elif not q or not p or q.val != p.val:
                return False
            
            return isSame(q.right, p.right) and isSame(p.left, q.left)
        
        if not root or not subRoot:
            return False
        
        elif root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
