# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0 or not head:
            return head
        dummy = ListNode('dummy')
        dummy.next = head
        p1 = p2 = dummy
        for _ in range(n):
            p2 = p2.next 
        # since n must be valid, p2 is not None here
        while p2.next is not None:
            p1, p2 = p1.next, p2.next
        p1.next = p1.next.next
        return dummy.next
