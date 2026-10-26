# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs
        self.count = 0
        
        def dfs(node, largest):
            if not node:
                return
            
            if node.val >= largest:
                self.count += 1
            
            dfs(node.left, max(node.val, largest))
            dfs(node.right, max(node.val, largest))

        dfs(root, root.val)
        return self.count