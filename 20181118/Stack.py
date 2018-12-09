from SinglyLinkedList import SinglyLinkedList

class Stack:
  def __init__(self):
    self.sll = SinglyLinkedList()

  def add(self, item):
    return self.sll.insert_front(item)

  def pop(self):
    return self.sll.remove_front()

  def peek(self):
    return self.sll.get(0)

  def size(self):
    return self.sll.size()