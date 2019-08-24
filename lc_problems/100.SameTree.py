# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if (not p and q) or (not q and p):
                return False
            if p and q:
                if p.val != q.val:
                    return False
                stack += [(p.left, q.left), (p.right, q.right)]
        return True
