from DoublyLinkedList import DoublyLinkedList

class Queue:
  def __init__(self):
    self.dll = DoublyLinkedList()

  def __repr__(self):
    tbp = ""
    temp_head = self.dll.head
    if self.dll.length == 0:
      return ""
    while temp_head.next:
      tbp += str(temp_head.item) + " <-> "
      temp_head = temp_head.next
    tbp += str(self.dll.tail.item)
    return tbp

  def enqueue(self, item):
    return self.dll.insert_back(item)

  def dequeue(self):
    return self.dll.remove_front()

  def size(self):
    return self.dll.size()

  def first(self):
    return self.dll.first()

  def last(self):
    return self.dll.last()