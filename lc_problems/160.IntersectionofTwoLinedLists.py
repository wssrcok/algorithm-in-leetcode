class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def approach3():
            if headA is None or headB is None:
                return None
            length = 0
            tempA, tempB = headA, headB
            while tempA:
                length += 1
                tempA = tempA.next
            while tempB:
                length += 1
                tempB = tempB.next
            tempA, tempB = headA, headB
            while tempA is not tempB and length:
                tempA = tempA.next if tempA.next else headB
                tempB = tempB.next if tempB.next else headA
                length -= 1
            return tempA if length else None
        def mine():
            lenA = lenB = 0
            tempA, tempB = headA, headB
            while tempA:
                lenA += 1
                tempA = tempA.next
            while tempB:
                lenB += 1
                tempB = tempB.next
            tempA, tempB = headA, headB
            if lenA > lenB:
                for _ in range(lenA - lenB):
                    tempA = tempA.next
            if lenA < lenB:
                for _ in range(lenB - lenA):
                    tempB = tempB.next
            while tempA is not None:
                if tempA is tempB:
                    return tempA
                tempA, tempB = tempA.next, tempB.next
            return None
        return mine()
    
