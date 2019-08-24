# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def backtrack(curr=[i for i in range(1, n+1)]):
            if len(curr) == 0:
                return [None]
            out = []
            for i in range(len(curr)):
                left, right = backtrack(curr[:i]), backtrack(curr[i+1:])
                for l in left:
                    for r in right:
                        node = TreeNode(curr[i])
                        node.left = l
                        node.right = r
                        out.append(node)
            return out

        return backtrack() if n else []
