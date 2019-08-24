# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        right = True
        out = []
        queue = collections.deque([root])
        while queue:
            l = len(queue)
            curr = []
            for _ in range(l):
                node = queue.popleft() if right else queue.pop()
                if node is None:
                    continue
                curr.append(node.val)
                if right:
                    queue += [node.left, node.right]
                else:
                    queue = collections.deque([node.left, node.right]) + queue
            out += [curr] if curr else []
            right = not right
        return out
