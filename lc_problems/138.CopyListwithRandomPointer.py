"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList_2pass(self, head: 'Node') -> 'Node':
        d = {}
        temp = head
        temp2 = out = Node('dummy')
        while temp:
            d[temp] = Node(temp.val)
            temp2.next = d[temp]   
            temp, temp2 = temp.next, temp2.next
        temp = head
        while temp:
            d[temp].random = d.get(temp.random, None)
            temp = temp.next
        return out.next
