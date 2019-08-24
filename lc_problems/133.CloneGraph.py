"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        out = Node(node.val, [])
        queue = collections.deque([(node, out)])
        d = {node:out}
        while queue:
            origin, new = queue.popleft()
            for neigh in origin.neighbors:
                if neigh not in d:
                    d[neigh] = Node(neigh.val, [])
                    queue.append((neigh, d[neigh]))
                new.neighbors.append(d[neigh])
        return out
