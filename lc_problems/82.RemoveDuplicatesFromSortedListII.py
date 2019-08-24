# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            if temp.next.val != temp.next.next.val:
                temp = temp.next
            else:
                curr = temp.next
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                temp.next = curr.next
        return dummy.next
