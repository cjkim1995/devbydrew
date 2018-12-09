from DoublyLinkedList import DoublyLinkedList

class Queue:
  def __init__(self):
    self.dll = DoublyLinkedList()

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