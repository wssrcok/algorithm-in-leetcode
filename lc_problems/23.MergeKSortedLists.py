# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = collections.deque(lists)
        while len(q) > 1:
            l1, l2 = q.popleft(), q.popleft()
            q.append(merge(l1, l2))
        return q.popleft()
    
    def merge(l1, l2):
        res = tail = ListNode('d')
        while l1 or l2:
            l1_val = l1.val if l1 else float('inf')
            l2_val = l2.val if l2 else float('inf')
            tail.next = l1 if l1_val < l2_val else l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tail = tail.next
        return res.next
