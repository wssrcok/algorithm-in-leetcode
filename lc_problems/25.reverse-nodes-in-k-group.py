#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        res = res_tail = ListNode('d')
        while True:
            if not self.ensure(head, k):
                res_tail.next = head
                break
            tail = head
            rev, head = self.reverse(head, k)
            res_tail.next = rev
            res_tail = tail
        return res.next

    def ensure(self, head, k):
        for _ in range(k):
            if not head:
                return False
            head = head.next
        return True

    def reverse(self, head, k):
        left = head
        right = head.next
        head.next = None
        for _ in range(k-1):
            then = right.next
            right.next = left
            left = right
            right = then
        return left, right
            
