# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node=root, _min=float('-inf'), _max=float('inf')):
            if node is None:
                return True
            if _min < node.val < _max:
                return validate(node.left, _min, node.val) and \
                       validate(node.right, node.val, _max)
            return False
