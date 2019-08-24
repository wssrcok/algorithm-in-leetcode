# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        dummy = TreeNode('d')
        dummy.left = root
        self.stack = [dummy]
        while self.stack[-1].left:
            self.stack.append(self.stack[-1].left)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
            while self.stack[-1].left:
                self.stack.append(self.stack[-1].left)
        return node.val
       
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
