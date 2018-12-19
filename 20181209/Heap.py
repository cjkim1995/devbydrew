class MinHeap:

  #indices:
    #self: i
    #left: 2 * i
    #right: 2 * i + 1
    #parent: i // 2
  
  def __init__(self):
    self.lst = [None]

  def insert(self, item):
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
    smol = self.lst[1]
    if len(self.lst) > 2:
      self.lst[1] = self.lst[len(self.lst) - 1]
      self.lst = self.lst[:-1]
      if len(self.lst) == 3:
        if self.lst[1] > self.lst[2]:
          self.lst[1], self.lst[2] = self.lst[2], self.lst[1]
        return smol

      i = 1
      left = 2 * i
      right = 2 * i + 1
      while self.lst[i] >= self.lst[left] or self.lst[i] >= self.lst[right]:
        if self.lst[left] < self.lst[right]:
          self.lst[i], self.lst[left] = self.lst[left], self.lst[i]
          i = 2 * i
        else:
          self.lst[i], self.lst[right] = self.lst[right], self.lst[i]
          i = 2 * i + 1
        left = 2 * i
        right = 2 * i + 1
        try:
          if self.lst[left] == None or not self.lst[right] == None:
            break
        except IndexError:
          break
      if len(self.lst) == 2:
        self.lst = self.lst[:-1]
      else:
        return None
    return smol


  def sort(self):
    result = []
    while len(self.lst):
      result.append(self.remove())
    return result









