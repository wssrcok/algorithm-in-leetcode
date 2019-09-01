# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        temp = dummy = ListNode('dummy')
        dummy.next = head
        while temp.next:
            start = temp.next
            _sum = 0
            while start:
                _sum += start.val
                if _sum == 0:
                    temp.next = start.next
                start = start.next
            temp = temp.next
        return dummy.next
