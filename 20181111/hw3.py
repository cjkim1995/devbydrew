hwtime = 0

#5
#sum all numbers from 1 to n
hwtime += 6
def nSum(n):
  if n == 1:
    return n
  else:
    return n + nSum(n-1)

#6
#return whether a string is a palindrome
hwtime += 4
def isPalindrome(string):
  # s = reversed(string)
  return string == string[::-1]

isPalindrome('abcba')


#7
#recursive method to compute x ** y
hwtime += 14
def myPow(x, y):
  if y == 1:
    return x
  if y == -1:
    return 1/x
  if y < 0:
    prod = myPow(x, y + 1)
    return 1 / x * prod
  if y > 0:
    prod = myPow(x, y - 1)
    return prod * x

myPow(2, -4)

#7b
#reduced time complexity recursive method to compute x ** y

def myRPow(x, y):
  if y == 1:
    return x
  if y == -1:
    return 1/x
  else:
    divy = y // 2
    result = myRPow(x, divy)
    if y % 2 == 0:
      return result * result
    else:
      if y > 0:
        return result * result * x
      else:
        return result * result * (1 / x)

myRPow(2,-4)

# def myRPow(x, y):
#     if y == 0:
#         return 1
#     divy = y // 2
#     result = myRPow(x, divy)
#     if y % 2 == 0:
#         return result * result
#     if y < 0:
#         if y == -1:
#             return 1 / x
#         if y % 2 == 0:
#             return result * result
#         else:
#             return result * result * (1 / x)
#     else:
#         return result * result * x

myRPow(2,-4)

#8
#recursively count how many 'x' exist in a string
hwtime += 15
def countX(string):
  count = 0
  if string[0] == 'x' or string[0] == 'X':
    count = 1
  if len(string) > 1:
    count += countX(string[1:])
  return count

countX('jaxbX')


#9
#recursively count how many 6s are in a list of ints with a starting index
hwtime += 10
def containsSix(s, index):
  if s[index] == 6:
    return True
  if len(s[index:]) > 1:
    return containsSix(s, index + 1)
  return False

containsSix([1, 5, 8, 6], 2)
containsSix([5, 2, 3, 1, 0], 1)

#10a
#recursively remove repeating adjacent characters
hwtime += 25
def cleanString(s):
  if len(s) == 0:
    return ''
  stringnew = ''
  if len(s) > 1:
    if s[0] == s[1]:
      s = s[1:]
    stringnew = cleanString(s[1:])
  if s[0] != stringnew:
    return s[0] + stringnew
  return s[0]

cleanString('helll')

#10b
#recursively remove repeating characters anywhere in string
hwtime += 50
def removeDuplicateCharacters(s):
  return removeDuplicateCharactersHelper(s, set())

def removeDuplicateCharactersHelper(s, seenChars):
  stringpart = ''
  stringnew = ''
  if len(s) >= 1:
    if s[0] not in seenChars:
      seenChars.add(s[0])
      stringpart = s[0]
    if len(s) > 1:
      stringnew = removeDuplicateCharactersHelper(s[1:],seenChars)
  return stringpart + stringnew

removeDuplicateCharacters('yyzzzabccyb')

#12
#recursive bubblesort
# def rBubSort(lst):
    # if lst[0] != min(lst)
hwtime += 45
def rBubSort(lst):
  next = []
  while lst[0] != min(lst):
    if lst[0] > lst[1]:
      lst[0], lst[1] = lst[1], lst[0]
    next = rBubSort(lst[1:])
    lst = [lst[0]] + next
  # zeroth = [lst[0]]
  # return zeroth + next
  return lst

a = [3, 6, 1, -55, 8, 10, -3]
rBubSort(a)


#13
#binary search
hwtime += 90
def binSearch(lst, val):
  if len(lst) == 0:
    return False
  else:
    key = len(lst)//2
    if lst[key] == val:
      return True
    else:
      if val < lst[key]:
        return binSearch(lst[:key], val)
      else:
        return binSearch(lst[key+1:], val)


b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
binSearch(b, 6)


#13b
#binary search iteratively

def binSearchIter(lst, val):
  assert len(lst) > 0
  start = 0
  end = len(lst) - 1
  while start <= end:
    key = (start + end) // 2
    if lst[key] < val:
      start = key + 1
    elif lst[key] > val:
      end = key - 1
    else:
      break
  return lst[key] == val  

binSearchIter(b, 3)
c = [1, 2, 2]
d = [-3, 0, 1, 4]
e = []
binSearchIter(c, 2)
binSearchIter(c, 1)
binSearchIter(d, -3)
binSearchIter(d, 0)
# binSearchIter(e, 0)


