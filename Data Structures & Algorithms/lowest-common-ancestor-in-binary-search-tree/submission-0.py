# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ancestor = root
        # check if node children contains p and q
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            mid = node.val == q.val or node.val == p.val
            if (left + right + mid) == 2 :
                self.ancestor = node

            # if node.val == p.val or node.val == q.val:
            #     return 1

            return left or right or mid

        dfs(root)
        return self.ancestor