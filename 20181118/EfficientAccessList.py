from DoublyLinkedList import DoublyLinkedList

class EfficientAccessList:
  def __init__(self):
    self.lookup = {}
    self.dll = DoublyLinkedList()
    
def size(self):
  # your code here
  return len(self.lookup)
    
def contains(self, item):
  """Returns whether the EfficientAccessList contains the given item."""
  # your code here
  return item in self.lookup

def insert(self, item):
  """Inserts item at the back of the list. Returns item."""
  # your code here
  return self.dll.insert(item)

def remove(self, item):
  """Removes item from the list, or does nothing if item is not in the list. Returns item if successfully removed, else None."""
  # your code here
  if self.contains(item):
    return self.dll.remove(item)
  return
