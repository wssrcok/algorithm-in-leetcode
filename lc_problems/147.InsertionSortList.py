# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode('dummy')
        dummy.next = head
        temp = head
        while temp.next:
            if temp.val <= temp.next.val:
                temp = temp.next
            else:
                node = temp.next
                temp.next = temp.next.next
                curr = dummy
                while curr.next.val < node.val:
                    curr = curr.next
                # now curr.next.val >= node.val
                then = curr.next
                curr.next = node
                node.next = then
        return dummy.next

                    



        
