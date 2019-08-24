"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        the key here is: 
        take use of the next pointer and try to connect the next level
        '''
        def recursion(node=root, right_node=None):
            return NotYetImplementedException()

        def bfs_without_queue(node=root):
            tail = dummy = TreeLinkNode(0)
            while node:
                tail.next = node.left
                if tail.next:
                    tail = tail.next
                tail.next = node.right
                if tail.next:
                    tail = tail.next
                node = node.next
                if not node:
                    tail = dummy
                    node = dummy.next
            # space is O(1)

        def bfs():
            queue = collections.deque([root])
            while queue:
                size = len(queue)
                prev = None
                for _ in range(size):
                    node = queue.popleft()
                    if node:
                        node.next = prev
                        prev = node
                        queue.append(node.right)
                        queue.append(node.left)
           # space is O(n)

        #recursion()
        bfs()
        return root

