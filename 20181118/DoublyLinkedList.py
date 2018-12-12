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
      self.head = rnode = DoublyLinkedListNode(item)
      self.tail = self.head
      return rnode
    prev_tail = self.tail
    self.tail = rnode = DoublyLinkedListNode(item, prev_tail)
    prev_tail.next = self.tail
    return rnode

  def size(self):
    return self.length

  def __repr__(self):
    tbp = ""
    temp_head = self.head
    if self.length == 0:
      return ""
    while temp_head.next:
      tbp += str(temp_head.item) + " <-> "
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

  def remove(self, item):
    if self.length > 0:
      curr_ph = self.head
      while curr_ph.item != item and curr_ph:
        curr_ph = curr_ph.next #iterate over the list until finding item
      if curr_ph.item == item: #find item
        self.length -= 1 #decrement by 1
        if curr_ph == self.head: #base case
          self.head = curr_ph.next #ju
          return curr_ph
        elif curr_ph == self.tail:
          self.tail = curr_ph.prev
          curr_ph.prev.next = None
          return curr_ph
        else:
          curr_ph.prev.next = curr_ph.next
          curr_ph.next.prev = curr_ph.prev
          return curr_ph
      return "No such item!"
      



class DoublyLinkedListNode:
  def __init__(self, item, prev = None, next = None):
    self.item = item
    self.prev = prev
    self.next = next

  def remove(self):
    # UPDATE THIS to handle removing head or tail
    self.prev.next = self.next
    self.next.prev = self.prev
    # probably also want to make self's pointers None
    self.prev = None
    self.next = None

