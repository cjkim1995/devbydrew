class singlyLinkedList:
  def __init__(self):
    self.head = None

  def find(self, item):
    tracking = self.head
    while tracking != None:
      if tracking.item == item:
        return tracking
      tracking = tracking.next
    return None
    

  def insert_i(self, item):
    if self.head == None:
      self.head = singlyLinkedListNode(item)
      return
    tobeinserted = self.head
    while tobeinserted.next != None:
      tobeinserted = tobeinserted.next
    tobeinserted.next = singlyLinkedListNode(item)
    
  def remove(self, item):
    tracking = self.head
    if tracking.item == item:
      self.head = tracking.next
      return
    while tracking != None:
      if tracking.next.item == item:
        tracking.next = tracking.next.next
        return
      tracking = tracking.next
    return tracking

  #<5 minutes
  def size(self):
    count = 0
    countcheck = self.head
    if countcheck == None:
      return count
    while countcheck != None:
      count += 1
      countcheck = countcheck.next
    return count

  #5 minutes
  def get(self, index):
    count = 0
    hold = self.head
    while True:
      if count == index:
        return hold.item
      hold = hold.next
      count += 1

  #45 minutes
  def insert_at(self, item, index):
    count = 0
    hold = self.head
    if index == 0:
      self.head, self.head.next = singlyLinkedListNode(item), self.head
      return
    while count < index - 1:
      hold = hold.next
      count += 1
    hold.next, hold.next.next = singlyLinkedListNode(item), hold.next


class singlyLinkedListNode:
  def __init__(self, item, next = None):
    self.item = item
    self.next = next

  # def insert_r(self, item):
  #   if self.next == None:
  #     self.next = singlyLinkedListNode(item)
  #   else:
  #     self.next.insert(item)


a = singlyLinkedList()
a.insert_i(4)
a.insert_i(2)
a.insert_i(5)
a.find(2)
a.find(3)
a.insert_at(100, 1)
a.size()
a.get(1)