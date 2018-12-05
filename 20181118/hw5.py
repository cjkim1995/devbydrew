class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def find(self, item):
    tracking = self.head
    while tracking != None:
      if tracking.item == item:
        return tracking
      tracking = tracking.next
    return None
    

  def insert_i(self, item):
    self.length += 1
    if self.head == None:
      self.head = SinglyLinkedListNode(item)
      return
    tobeinserted = self.head
    while tobeinserted.next != None:
      tobeinserted = tobeinserted.next
    tobeinserted.next = SinglyLinkedListNode(item)
    
  def remove(self, item):
    tracking = self.head
    if tracking.item == item:
      self.head = tracking.next
      self.length -= 1
      return
    while tracking != None:
      if tracking.next.item == item:
        tracking.next = tracking.next.next
        self.length -= 1
        return
      tracking = tracking.next
    return tracking

  #<5 minutes
  def size(self):
    return self.length

  #5 minutes
  def get(self, index):
    count = 0
    hold = self.head
    if index > self.length:
      return
    while True:
      if count == index:
        return hold.item
      hold = hold.next
      count += 1

  #45 minutes
  def insert_at(self, item, index):
    self.length += 1
    count = 0
    hold = self.head
    if index == 0:
      self.head, self.head.next = SinglyLinkedListNode(item), self.head
      return
    while count < index - 1:
      hold = hold.next
      count += 1
    hold.next, hold.next.next = SinglyLinkedListNode(item), hold.next

  def insert_front(self, item):
    return self.insert_at(item, 0)

  def remove_front(self):
    if self.length == 0:
      return
    prev_head = self.head
    self.head = self.head.next
    return prev_head.item



class SinglyLinkedListNode:
  def __init__(self, item, next = None):
    self.item = item
    self.next = next

  # def insert_r(self, item):
  #   if self.next == None:
  #     self.next = SinglyLinkedListNode(item)
  #   else:
  #     self.next.insert(item)


a = SinglyLinkedList()
a.insert_i(4)
a.insert_i(2)
a.insert_i(5)
a.find(2)
a.find(3)
a.insert_at(100, 1)
a.size()
a.get(1)


#initialize + constructor took ~20 min
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def first(self):
    return self.head.item

  def last(self):
    return self.tail.item

  def insert(self, item):
    self.length += 1
    if self.head == None:
      self.head = DoublyLinkedListNode(item)
      self.tail = self.head
      return
    prev_tail = self.tail
    self.tail = DoublyLinkedListNode(item, prev_tail)
    prev_tail.next = self.tail

  def size(self):
    return self.length

  def __repr__(self):
    tbp = ""
    temp_head = self.head
    if self.length == 0:
      return ""
    while temp_head.next:
      tbp += str(temp_head.item) + " -> "
      temp_head = temp_head.next
    tbp += str(self.tail.item)
    return tbp

  def __str__(self):
    pass

  def insert_back(self, item):
    return self.insert(item)

  def insert_front(self, item):
    self.length += 1
    prev_head = self.head
    self.head = DoublyLinkedListNode(item)
    self.head.next = prev_head
    if self.length == 1:
      self.tail = self.head
    else:
      prev_head.prev = self.head
    return

  def remove_front(self):
    if self.length > 0:
      self.length -= 1
      self.head = self.head.next
      if self.length == 0:
        self.tail = None
        return
      self.head.prev = None
    return

  def remove_back(self):
    if self.length > 0:
      self.length -= 1
      self.tail = self.tail.prev
      if self.length == 0:
        self.head = None
        return
      self.tail.next = None
      return

    return


class DoublyLinkedListNode:
  def __init__(self, item, prev = None, next = None):
    self.item = item
    self.prev = prev
    self.next = next



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



def dll_test1():
  b = DoublyLinkedList()
  b.insert(1)
  b.insert(2)
  b.insert(3)

  assert b.head.item == 1, 'Head is not one'
  assert b.head.next.item == 2, 'Second node is not 2'
  assert b.length == 3, 'Length is not 3'
  assert b.tail.item == 3, 'Tail is not 3'

  return 0

def dll_test2():
  """
  What is this testing?
  """

  return 0

  c.insert_front(0)
  c.insert_back(1)
  c.insert_back(2)


b = DoublyLinkedList()
b.insert(1)
b.insert(2)
b.insert(3)


c = DoublyLinkedList()
c.insert_front(0)
c.insert_back(1)
c.insert_back(2)
c.remove_front()


# if __name__ == '__main__':
#   dll_test1()
#   dll_test2()

#   print("All tests passed!")