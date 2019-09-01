#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left == right:
            return 2**left - 1 + self.countNodes(root.right) + 1
        else:
            return self.countNodes(root.left) + 2**right - 1 + 1

    def height(self, node):
        if node is None:
            return 0
        return 1 + self.height(node.left)
            

