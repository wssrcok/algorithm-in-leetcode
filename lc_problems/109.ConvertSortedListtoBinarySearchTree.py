# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head:
            mid = tail = head
            premid = None
            while tail and tail.next:
                premid, mid, tail = mid, mid.next, tail.next.next
            if premid:
                premid.next = None
            root = TreeNode(mid.val)
            root.left = self.sortedListToBST(head if head is not mid else None)
            root.right = self.sortedListToBST(mid.next)
            return root
            
    def sortedListToBST_optimized(self, head: ListNode) -> TreeNode:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        def inorder(i=0, j=length-1):
            nonlocal head
            if j < i:
                return None
            m = i + (j - i) // 2
            left = inorder(i, m - 1)
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = inorder(m + 1, j)
            return root
        return inorder()
            
