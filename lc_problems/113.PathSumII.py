# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        out = []
        def explore(node=root, s=sum, curr=[]):
            if node is None:
                return
            if not node.left and not node.right:
                if node.val == s:
                    out.append(curr + [node.val])
            else:
                explore(node.left, s-node.val, curr + [node.val])
                explore(node.right, s-node.val, curr + [node.val])
        explore()
        return out
