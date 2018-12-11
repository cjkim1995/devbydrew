from SinglyLinkedList import SinglyLinkedList

class Stack:
  def __init__(self):
    self.sll = SinglyLinkedList()

  def __repr__(self):
    temp = ""
    head_temp = self.sll.head
    if self.sll.length == 0:
      return ""
    while head_temp.next:
      temp += str(head_temp.item) + " -> "
      head_temp = head_temp.next
    temp += str(head_temp.item)
    return temp

  def add(self, item):
    return self.sll.insert_front(item)

  def pop(self):
    return self.sll.remove_front()

  def peek(self):
    return self.sll.get(0)

  def size(self):
    return self.sll.size()