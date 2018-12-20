class MinHeap:

  #indices:
    #self: i
    #left: 2 * i
    #right: 2 * i + 1
    #parent: i // 2
  
  def __init__(self):
    self.lst = [None]

  def insert(self, item):
    assert isinstance(item, int), 'Integers only!'
    self.lst.append(item)
    if len(self.lst) > 2:
      idx = len(self.lst) - 1
      while self.lst[idx] < self.lst[idx // 2]:
        if idx >= 1:
          self.lst[idx], self.lst[idx // 2] = self.lst[idx // 2], self.lst[idx]
          if idx // 2 > 1:
            idx = idx // 2
          else:
            break


  def remove(self):
    if len(self.lst) <= 1: #base case
      return None
    smol = self.lst[1] #placeholder for node to be removed
    if len(self.lst) == 2:
      self.lst = self.lst[:-1] #remove the single node & return
      return smol
    elif len(self.lst) > 2:
      self.lst[1] = self.lst[-1] #replace the root node with last node
      self.lst = self.lst[:-1] #remove last node
      if len(self.lst) == 3: #if only two nodes, keep it simple
        if self.lst[1] > self.lst[2]:
          self.lst[1], self.lst[2] = self.lst[2], self.lst[1]
        return smol

      lidx = len(self.lst) - 1 #initialize often used index
      i = 1
      left = 2 * i
      right = 2 * i + 1
      while (right <= lidx and left <= lidx) and (self.lst[i] >= self.lst[left] or self.lst[i] >= self.lst[right]): #while right&left do not raise IndexError & heap property not fulfilled
        if self.lst[left] < self.lst[right]:
          self.lst[i], self.lst[left] = self.lst[left], self.lst[i]
          i = 2 * i
        else:
          self.lst[i], self.lst[right] = self.lst[right], self.lst[i]
          i = 2 * i + 1
        left = 2 * i
        right = 2 * i + 1
        if left > lidx or right > lidx:
          break
    return smol


  def min(self):
    return self.lst[1]

  # def sort(self):
  #   result = []
  #   while len(self.lst) > 1:
  #     result.append(self.remove())
  #   return result

  def size(self):
    return len(self.lst) - 1


  def bottomUpHeap(self, arr):
    # self = i
    # parent = i // 2
    # left = i * 2
    # right = i * 2 + 1
    idx = (len(arr) - 1) // 2 #initialize index to be the parent node of last node
    j = len(arr) // 2 #supposed to be an indicator of number of checks that have to be taken 
    while j > 0 and len(arr) > 2: #while steps remain and more than 1 node
      try:
        if arr[idx] > arr[idx * 2 + 1]: #swap if parent is larger than right, try/except used due to potential IndexError if the right node does not exist
          arr[idx], arr[idx * 2 + 1] = arr[idx * 2 + 1], arr[idx]
      except IndexError:
        pass
      if arr[idx] > arr[idx * 2]: #swap if parent is larger than left
        arr[idx], arr[idx * 2] = arr[idx * 2], arr[idx]
      j -= 1 #decrement steps
      idx -= 1 #decrement parent node
    self.lst = arr
    return self.lst


