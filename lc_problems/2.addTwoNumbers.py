def addTwoNumbers(self, l1, l2):
  c = 0
  dummy = ListNode("dummy")
  temp = dummy
  while l1 and l2:
    s = l1.val + l2.val + c
    temp.next = ListNode(s % 10)
    c = s // 10
    temp, l1, l2 = temp.next, l1.next, l2.next
  
  while l1:
    s = l1.val + c
    temp.next = ListNode(s % 10)
    c = s // 10
    temp, l1 = temp.next, l1.next

  while l2:
    s = l2.val + c
    temp.next = ListNode(s % 10)
    c = s // 10
    temp, l2 = temp.next, l2.next

  if c:
    temp.next = ListNode(1)

  return dummy.next
