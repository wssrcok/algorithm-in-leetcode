# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            head, tail = self.quickSort(head)
        return head

    def mergeSort(self, head):
        def merge(head1, head2):
            tail = out = ListNode('d')
            while head1 and head2:
                if head1.val < head2.val:
                    tail.next = head1
                    head1 = head1.next
                else:
                    tail.next = head2
                    head2 = head2.next
                tail = tail.next
            tail.next = head1 or head2
            return out.next

        q = collections.deque()
        while head:
            q.append(head)
            head, head.next = head.next, None
        while len(q) > 1:
            left, right = q.popleft(), q.popleft()
            q.append(merge(left, right))
        return q.pop()

    def quickSort(self, head):
        '''
        head is never None
        '''
        if head.next is None:
            return head, head
        lt = lt_tail = ListNode('d')
        ge = ge_tail = ListNode('d')
        while head.next:
            if head.next.val < head.val:
                lt_tail.next = head.next
                lt_tail = lt_tail.next
            else:
                ge_tail.next = head.next
                ge_tail = ge_tail.next
            head.next = head.next.next
        lt_tail.next = None
        ge_tail.next = None
        left_head, left_tail = self.quickSort(lt.next) if lt.next else (head, head)
        right_head, right_tail = self.quickSort(ge.next) if ge.next else (head, head)
        if left_tail is not head and right_head is not head:
            left_tail.next = head
            head.next = right_head
        elif left_tail is not right_head:
            left_tail.next = right_head
        return left_head, right_tail
