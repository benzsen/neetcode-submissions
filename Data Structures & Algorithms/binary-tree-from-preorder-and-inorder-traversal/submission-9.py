# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: i for i, val in enumerate(inorder)}
        self.pre = 0

        # r/l is for inorder
        def dfs(l, r):
            if l > r:
                return None

            root = TreeNode(preorder[self.pre])
            i = indices[root.val] 
            
            self.pre += 1
            root.left = dfs(l,i-1)
            root.right = dfs(i+1,r)

            return root

        return dfs(0, len(inorder) - 1)