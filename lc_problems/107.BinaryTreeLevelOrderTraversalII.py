# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        out = []
        def recursion(node=root, level=0):
            if node is not None:
                if len(out) == level:
                    out.append([])
                out[level].append(node.val)
                recursion(node.left, level + 1)
                recursion(node.right, level + 1)
        recursion()
        return out[::-1]
