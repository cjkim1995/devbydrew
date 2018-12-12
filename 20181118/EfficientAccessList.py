from DoublyLinkedList import DoublyLinkedList, DoublyLinkedListNode

class EfficientAccessList:
  def __init__(self):
    self.lookup = {}
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

  # running time: O(1)
  def size(self):
    # your code here
    # return self.dll.size() # runs in O(1)
    return len(self.lookup) #dictionary len is len of the list
      
  # running time: O(1)
  def contains(self, item):
    """Returns whether the EfficientAccessList contains the given item."""
    # your code here
    return item in self.lookup

  # running time: O(1)
  def insert(self, item):
    """Inserts item at the back of the list. Returns item."""
    # your code here
    # self.lookup[len(self.lookup) + 1] = item #add key:val::index:item
    inserted_node = self.dll.insert(item)
    self.lookup[item] = inserted_node

    return inserted_node

  # running time: currently O(n)
  # this should run in O(1)
  # 
  def remove(self, item):
    """Removes item from the list, or does nothing if item is not in the list. Returns item if successfully removed, else None."""
    # your code here
    if self.contains(item):
      # keys = [k2 for (k1, value) in self.lookup.items() if value == item] #list comprehension to find key indices that match the item value
      # self.lookup.pop(keys[0]) #remove the first instance of the value, by key index, from dic
      node_to_remove = self.lookup[item]
      node_to_remove.remove() # remove from list
      del self.lookup[item] # remove from dictionary
      return item
