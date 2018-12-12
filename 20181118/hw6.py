from Stack import Stack


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
  # assert c, "s3 failed"
  # assert d, "s4 failed"
  return 0


#merge sorted (linked) lists
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

#3+ hours
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

  if l1 == None or l2 == None:
    if l1 == None: #checks for if any lists are empty
      return l2
    else:
      return l1
  
  l3 = l4 = ListNode(0) #initialize placeholder, get two pointers to same placeholder
  while l1 and l2: 
    if l1.val <= l2.val:
      l3.next = l1
      l1 = l1.next
    else:
      l3.next = l2
      l2 = l2.next
    l3 = l3.next
  l3.next = l1 or l2
  return l4.next




a1 = ListNode(1)
a1.next = ListNode(2)
a1.next.next = ListNode(4)
a2 = ListNode(1)
a2.next = ListNode(3)
a2.next.next = ListNode(4)

def mergeTwoLists_test():  
  merged = mergeTwoLists(a1, a2)
  assert merged.val is 1
  assert merged.next.val is 1
  assert merged.next.next.val is 2
  assert merged.next.next.next.val is 3
  assert merged.next.next.next.next.val is 4
  assert merged.next.next.next.next.next.val is 4
  assert merged.next.next.next.next.next.next is None
  return 0
  
#45 min
def deleteDuplicates(head):
  """
  :type head: ListNode
  :rtype: ListNode
  Input: 1 -> 1 -> 2
  Output: 1 -> 2
  """
  if head == None: #return just the list if length is <= 1
    return head
  elif head.next == None:
    return head
  else:
    seen = set() #initialize set
    l3 = l4 = ListNode(0) #two pointers to same initial placeholder linkedlist
    while head: #iterate over input
      if head.val not in seen: #check if val is in set
        seen.add(head.val) #add unique vals
        l3.next = ListNode(head.val) #add val to linkedlist
        l3 = l3.next #first pointer to next of itself
      head = head.next 
    return l4.next #return next of second pointer, which is the whole list

b1 = ListNode(1)
b1.next = ListNode(1)
b1.next.next = ListNode(2)

def deleteDuplicates_test():
  chk = deleteDuplicates(b1)
  assert chk.val is 1
  assert chk.next.val is 2
  assert chk.next.next is None
  return 0




#15 min
def middleNode(head):
  """
  :type head: ListNode
  :rtype: ListNode
  input: 1 -> 2 -> 3 -> 4 -> 5
  output: 3 -> 4 -> 5
  if even count, return second half
  """
  if head.next == None:
    return head
  count = 0
  l3 = l4 = head #can't unpack listnode, point separately
  while l3:
    count += 1 #find length of linkedlist
    l3 = l3.next
  for i in range(count // 2): #step by step for // 2 of length for second pointer
    l4 = l4.next
  return l4

c1 = ListNode(1)
c1.next = ListNode(2)
c1.next.next = ListNode(3)
c1.next.next.next = ListNode(4)
c1.next.next.next.next = ListNode(5)

def middleNode_test():
  assert middleNode(c1).val is 3
  assert middleNode(c1).next.val is 4
  assert middleNode(c1).next.next.val is 5
  assert middleNode(c1).next.next.next is None
  return 0 


#45 min
def reverseList(head):
  """
  :type head: ListNode
  :rtype: ListNode
  input: 1 -> 2 -> 3 -> 4 -> 5 -> None
  output: 5 -> 4 -> 3 -> 2 -> 1 -> None
  """
  # l3 = head
  # l4 = head
  # l5, l6 = ListNode(0)
  # while l3.next:
  #   l3 = l3.next
  # while l3 != l4:
  #   l5.next = ListNode(l3.val)
  l3 = head
  l4 = l5 = ListNode(0) #two pointers to new LinkedList
  lst = [] #initialize list to store values
  while l3:
    lst.append(l3.val) #store linkedlist vals in lst
    l3 = l3.next
  lst.reverse() #reverse list
  for i in lst:
    l4.next = ListNode(i) #create new linkedlist using reversed list
    l4 = l4.next
  return l5.next #return original linkedlist using second pointer

def reverseList_test():
  chk = reverseList(c1)
  assert chk.val is 5
  assert chk.next.val is 4
  assert chk.next.next.val is 3
  assert chk.next.next.next.val is 2
  assert chk.next.next.next.next.val is 1
  assert chk.next.next.next.next.next is None
  return 0

if __name__ == '__main__':
  parentheses_test()
  mergeTwoLists_test()
  deleteDuplicates_test()
  middleNode_test()
  reverseList_test()

  print("All tests passed!")