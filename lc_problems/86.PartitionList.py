# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less, greater = ListNode(0), ListNode(0)
        less_tail, greater_tail = less, greater
        while head:
            if head.val < x:
                less_tail.next = head 
                less_tail = less_tail.next
            else:
                greater_tail.next = head
                greater_tail = greater_tail.next
            head = head.next
        less_tail.next = greater.next
        greater_tail.next = None
        return less.next
