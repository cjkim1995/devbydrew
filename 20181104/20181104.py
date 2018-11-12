import random

#bucketsorts n entries into k discrete buckets, O(n + k) -> O(n)
def bucketSort(lst):
  vals = set(lst)
  bigdic = {}
  sortedOutput = []
  for elem in lst:
    if elem in bigdic:
      bigdic[elem].append(elem)
    else:
      bigdic[elem] = [elem]
  for j in vals:
    sortedOutput.extend(bigdic[j])
  return sortedOutput

lsttry = []
lsttry2 = []
for k in range(0, 10):
  lsttry.append(random.randint(0,5))
  lsttry2.append(random.randint(0,5))

def bucketSort2(lst):
  bigdic = {}
  sortedOutput = []
  for elem in lst:
    if elem in bigdic:
      bigdic[elem].append(elem)
    else:
      bigdic[elem] = [elem]
  for j in range(min(lst), max(lst) + 1):
    if j not in bigdic:
      pass
    else:
      sortedOutput.extend(bigdic[j])
  return sortedOutput



#quicksort
def quickSort(lst):
  part = lst[-1:]
  if len(lst) <= 1:
    return part
  else:
    left, right = [], []
    for i in range(len(lst)-1):
      if lst[i] <= part[0]:
        left.append(lst[i])
      else:
        right.append(lst[i])
    left = quickSort(left)
    right = quickSort(right)
    return left + part + right


#binary search
def binarySearch(sortedlst, target):
  midIndex = len(sortedlst) // 2
  if target == sortedlst[midIndex]:
    return True
  elif target > sortedlst[midIndex]:
    binarySearch(sortedlst[midIndex:], target)
  elif target < sortedlst[midIndex]:
    binarySearch(sortedlst[:midIndex + 1], target)
    return False

b = sorted([1, 3, 5, 6, 8, 9, 10])
binarySearch(b, 7)
binarySearch(b, 8)