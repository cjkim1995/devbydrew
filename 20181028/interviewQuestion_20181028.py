"""import time"""

#Given a list of numbers and a target number, check to see that there are two elements that sum to the target
def checkLst(lst, target):
  """for i in range(len(lst)):
          for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
              return True
        return False"""
  for i in lst:
    if target - i in lst:
      return True
  return False

a = [2, -5, 10, 4, 7]
'''preTime1 = time.time()'''
b = checkLst(a, 6)
'''postTime1 = time.time()'''
print(b)
#This gives time complexity of O(n**2)

#We try to use dictionaries to get O(n) time complexity
def checkLstDict(lst, target):
  dct = {}
  for i in lst:
    dct[i] = 0
    if target - i in dct:
      return True
  return False


"preTime2 = time.time()"
c = checkLstDict(a, 6)
"""postTime2 = time.time()
print(c)"""

"""diffTime1 = postTime1 - preTime1
diffTime2 = postTime2 - preTime2
print(diffTime1)
print(diffTime2)
"""

Lst1 = [10, 5, 38, 25]
Lst2 = [10, 7, 2, 3, 8]
val1 = 48
val2 = 16
val3 = 6
cl1 = checkLst(Lst1, val1)
cl2 = checkLst(Lst1, val2)
cd1 = checkLstDict(Lst1, val1)
cd2 = checkLstDict(Lst1, val2)
print(cl1, cl2, cd1, cd2)

cd3 = checkLstDict(Lst2, val3)
print(cd3)

def checkLstDictFixed(lst, target):
  seen_nos = {}
  for num in lst:
    if target - num in seen_nos:
      return True
    seen_nos[num] = 0
  return False

cdd1 = checkLstDictFixed(Lst1, val1)
cdd2 = checkLstDictFixed(Lst1, val2)
cdd3 = checkLstDictFixed(Lst2, val3)
print(cdd1, cdd2, cdd3)