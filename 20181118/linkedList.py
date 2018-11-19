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