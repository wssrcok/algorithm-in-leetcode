class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.old = self.ListNode('dummy', 'dummy')
        self.new = self.ListNode('dummy', 'dummy')
        self.old.next, self.new.prev = self.new, self.old
        self.d = {}  # pair  key:ListNode(val)
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        node = self.d[key]
        # remove node from it's neighbor
        if node.prev and node.next:
            node.prev.next, node.next.prev = node.next, node.prev
        # add neighbor for node
        node.prev, node.next = self.new.prev, self.new
        # add node for neighbor
        self.new.prev.next, self.new.prev = node, node
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.get(key)
            self.d[key].val = value
        else:
            self.d[key] = self.ListNode(key, value)
            self.get(key)  # adding node to the end
            if self.capacity == 0:
                if self.old.next is self.new:
                    return
                old_node = self.old.next
                del self.d[old_node.key]
                old_node.next.prev = self.old
                self.old.next = old_node.next
            else:
                self.capacity -= 1

    class ListNode(object):
        def __init__(self, key, val, prev=None, next=None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next
