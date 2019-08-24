# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + min(self.minDepth(root.left) if root.left else float('inf'), self.minDepth(root.right) if root.right else float('inf'))
