from hw5 import Queue, Stack

def parentheses(string):
  seen = Stack()
  opening = ['(', '[', '{']
  match = {')':'(', ']':'[', '}':'{'}
  if len(string) % 2 != 0:
    return False
  for char in string:
    if char in opening:
      seen.add(char)
    else:
      if seen.size() == 0:
        return False
      else:
        if match[char] != seen.pop():
          return False
  return True

s1 = '([{}])'
s2 = '()[]'
s3 = '([)]'
s4 = '('

def parentheses_test():
  a = parentheses(s1)
  b = parentheses(s2)
  c = parentheses(s3)
  d = parentheses(s4)
  assert a, "s1 failed"
  assert b, "s2 failed"
  assert c, "s3 failed"
  assert d, "s4 failed"
  return 0


#merge sorted (linked) lists
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def insert(self, item):
    if self.val == None:
      self.val = ListNode(item)
      return
    tobeinserted = self
    while tobeinserted.next != None:
      tobeinserted = tobeinserted.next
    tobeinserted.next = ListNode(item)

#merge sorted singly linked lists
def mergeTwoLists(l1, l2):
  """
  :type l1: ListNode
  :type l2: ListNode
  :rtype: ListNode
  """

  # if l1.val != None and l2.val != None and l1.val <= l2.val: #choose an initial list (with minimum start value)
  #   l3 = l1
  # elif l1.val != None and l2.val != None and l1.val > l2.val:
  #   l3 = l2

  if l1.val <= l2.val:
    l3 = ListNode(l1.val)
    l1 = l1.next
  else:
    l3 = ListNode(l2.val)
    l2 = l2.next
  
  # while l1.val != None or l2.val != None:
  #   if l1 == None:
  #     l3_ph = l3.next
  #     l3.next = ListNode(l2.val)
  #     l3.next.next = l3_ph
  #     l2 = l2.next
  #   elif l2 == None:
  #     l3_ph = l3.next
  #     l3.next = ListNode(l1.val)
  #     l3.next.next = l3_ph
  #     l1 = l1.next
  #   elif l1.val <= l2.val:
  #     l3_ph = l3.next
  #     l3.next = ListNode(l1.val)
  #     l3.next.next = l3_ph
  #     l1 = l1.next
  #   else:
  #     l3_ph = l3.next
  #     l3.next = ListNode(l2.val)
  #     l3.next.next = l3_ph
  #     l2 = l2.next
  # return l3

  while l1 != None or l2 != None:
    if l1 == None:
      l3.insert(l2.val)
      l2 = l2.next
    elif l2 == None:
      l3.insert(l1.val)
      l1 = l1.next
    elif l1.val <= l2.val:
      l3.insert(l1.val)
      l1 = l1.next
    elif l2.val < l1.val:
      l3.insert(l2.val)
      l2 = l2.next
  return l3



def mergeTwoLists_test():
  a1 = ListNode(1)
  a1.next = ListNode(2)
  a1.next.next = ListNode(4)
  a2 = ListNode(1)
  a2.next = ListNode(3)
  a2.next.next = ListNode(4)
  
  return mergeTwoLists(a1, a2)
  


if __name__ == '__main__':
  parentheses_test()
  

  print("All tests passed!")