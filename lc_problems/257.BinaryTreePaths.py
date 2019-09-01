# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        stack = [(root, '')]
        res = []
        while stack:
            node, s = stack.pop()
            s += '->' + str(node.val)
            if node.left:
                stack.append((node.left, s))
            if node.right:
                stack.append((node.right, s))
            if not node.left and not node.right:
                res.append(s[2:])
        return res
                
