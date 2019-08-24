# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find node before mid point
        slow = fast = dummy = ListNode('dummy')
        dummy.next = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        # reverse mid
        reversed_mid = self.reverseList(mid)
        # combine two lists
        self.combine(head, reversed_mid)

    def combine(self, head1, head2):
        while head2:
            t1 = head1.next
            head1.next = head2
            head2 = head2.next
            head1.next.next = t1
            head1 = head1.next.next

    def reverseList(self, head):
        left = None
        right = head
        while right:
            then = right.next
            right.next = left
            left = right
            right = then
        return left
