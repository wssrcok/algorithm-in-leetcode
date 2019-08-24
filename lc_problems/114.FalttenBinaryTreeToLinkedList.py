# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def flatten_reversed_preorder(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root

        def flatten_morris_traversal(self, root: TreeNode) -> None:
        if not root:
            return

        # using Morris Traversal of BT
        node=root

        while node:
            if node.left:
                pre=node.left
                while pre.right:
                    pre=pre.right
                pre.right=node.right
                node.right=node.left
                node.left=None
            node=node.right

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        if not root.left and not root.right:
            return root
        left, right = root.left, root.right
        left_tail = self.flatten(left)
        right_tail = self.flatten(right)
        if left_tail:
            root.right = left
            root.left = None
            left_tail.right = right
        return right_tail if right_tail else left_tail
        
