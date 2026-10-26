# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs
        self.count = 1
        # def dfs(node):
        #     if not node:
        #         return 0
            
        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     if node.val < left: self.count += 1
        #     if node.val < right: self.count += 1 

        #     return node.val
        
        def dfs(node, largest):
            left = node.left 
            right = node.right

            if left:
                if left.val >= largest:
                    self.count += 1
                dfs(left, max(left.val, largest))

            if right:
                if right.val >= largest:
                    self.count += 1
                dfs(right, max(right.val, largest))

            else: return 

        dfs(root, root.val)
        return self.count