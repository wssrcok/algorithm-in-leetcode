# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs_iterative(self, head: ListNode) -> ListNode:
        dummy = ListNode("dummy")
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            t1 = p.next
            t2 = p.next.next
            t1.next = t2.next
            t2.next = t1
            p.next = t2
            p = p.next.next
        return dummy.next
    
    def swapPairs_recursive(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        _next = head.next
        _nextnext = self.swapPairs_recursive(head.next.next)
        _next.next = head
        head.next = _nextnext
        return _next

