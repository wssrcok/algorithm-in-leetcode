class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        before = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m-1):
            before = before.next
        left = before.next
        right = left.next
        left.next = None
        tail = left
        for _ in range(n-m):
            then = right.next
            right.next = left
            left = right
            right = then
        start.next = left
        tail.next = then
        return dummy.next
        


    def reverseBetween_recursive(self, head: ListNode, m: int, n: int) -> ListNode:
        
        def reverse(curr=head, M=m-1, N=n-1):
            if M > 0:
                curr.next = reverse(curr.next, M-1, N-1)
                return curr
            elif N > 0:
                last = reverse(curr.next, M-1, N-1)
                curr.next.next = curr
                return last
            else:
                return curr.next
        return reverse()
            
