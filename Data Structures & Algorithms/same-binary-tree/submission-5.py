# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(node, sub):
            if not node and not sub:
                return True
            
            if not node or not sub or node.val != sub.val:
                return False

            if node.val == sub.val:
                return isSame(node.left, sub.left) and isSame(node.right, sub.right)
        
        return isSame(p, q)