class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.length = 0


  def __repr__(self):
    temp = ""
    head_temp = self.head
    if self.length == 0:
      return ""
    while head_temp.next:
      temp += str(head_temp.item) + " -> "
      head_temp = head_temp.next
    temp += str(head_temp.item)
    return temp


  def find(self, item):
    tracking = self.head
    while tracking != None:
      if tracking.item == item:
        return tracking
      tracking = tracking.next
    return None
    

  def insert(self, item):
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