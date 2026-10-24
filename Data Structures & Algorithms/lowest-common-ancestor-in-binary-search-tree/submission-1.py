# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = root
        # mid, left, right
        # using bool 0/1 for False/True
        def dfs(node):
            if not node:
                return 0

            mid = 1 if node is p or node is q else 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if mid + left + right == 2:
                self.res = node
                
            return mid or left or right
        
        dfs(root)
        return self.res