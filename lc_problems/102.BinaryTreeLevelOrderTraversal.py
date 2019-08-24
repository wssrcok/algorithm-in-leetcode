# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque([(root, 0)])
        out = []
        while queue:
            node, level = queue.popleft()
            if node is not None:
                if len(out) == level:
                    out.append([node.val])
                else:
                    out[-1].append(node.val)
                queue += [(node.left, level+1), (node.right, level+1)]
        return out
