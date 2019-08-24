# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recurse(prev=None, curr=head):
            if curr.next is None:
                return curr 
            last = recurse(curr, curr.next)
            curr.next = prev
            return last 
        return recurse()
