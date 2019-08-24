# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root, root)]
        while stack:
            p, q = stack.pop()
            if (not p and q) or (not q and p):
                return False
            if p and q:
                if q.val != p.val:
                    return False
                stack += [(p.left, q.right), (p.right, q.left)]
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        queue = collections.deque([(root, root)])
        while queue:
            p, q = queue.popleft()
            if (not p and q) or (not q and p):
                return False
            if p and q:
                if q.val != p.val:
                    return False
                queue += [(p.left, q.right), (p.right, q.left)]
        return True

