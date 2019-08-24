# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode, curr=0) -> int:
        if root:
            left = right = 0
            if root.left:
                left = self.sumNumbers(root.left, curr*10+root.val)
            if root.right:
                right = self.sumNumbers(root.right, curr*10+root.val)
            if not left and not right:
                return curr*10+root.val
            return left + right
        return 0
