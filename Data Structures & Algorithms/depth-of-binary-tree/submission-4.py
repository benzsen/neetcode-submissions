# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # contract: takes in a node, returns depth count of a node
        # assume self.maxDepth works (Will return depth)
        
        # base case
        if not root:
            return 0
        
        # work for one node + return
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))