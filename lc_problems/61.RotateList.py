# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        last = head
        length = 1
        while last.next is not None:
            last = last.next
            length += 1
        k = k % length
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
        last.next = head
        head = temp.next
        temp.next = None
        return head
        
