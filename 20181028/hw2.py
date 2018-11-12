import random

hwtime = 0

a = []
for j in range(10):
    a.append(random.randint(-20,20))
#1
#Manual maximum function
hwtime += 7

def myMax(lst):
  mymax = lst[0] #Assign the first value of the list as the max
  for i in range(len(lst)-1): #Try to disprove that the first value is the max, iteratively
    if mymax < lst[i+1]:
      mymax = lst[i+1] #if disproven, reassign the victor as the new max
  return mymax

lst1 = [5, 1, 7, -8, 12]
myMax(a)
myMax(lst1)


#2
#Return key for highest value in dictionary
hwtime += 3

def highestVal(dic1):
  dic1Vals = dic1.values() #values of dictionary
  maxDic1Vals = max(dic1Vals) #max of values
  for key, item in dic1.items():
    if item == maxDic1Vals: #find key for max value from dictionary
      return key

d1 = {'e':1, 'd':2, 'c':3, 'b':4, 'a':5}
highestVal(d1)


#3
#Return longest string in a list
hwtime += 7

def longestString(lstString):
  lens = [] #initialize list
  for string in lstString:
    lens.append(len(string)) #append respective lengths of each string to another list
  return lstString[lens.index(max(lens))] #use fact that indices match to recall longest string

str1 = ['fds', 'qtwet', 'gdasfsa', 're']
longestString(str1)


#4
#Return count of how many prime numbers in list
hwtime += 12

def isPrime(number):
  if number < 2: #1 and below are non-prime
    return False
  for divisors in range(2, number): #anything from 2 to the actual number should not divide number evenly
    if number % divisors == 0:
      return False
  else:
    return True

def primeCount(lst1):
  count = 0 #initialize count
  for elem in lst1:
    if isPrime(elem):
      count += 1 #add to count if prime
  return count

primeLst = [3, 6, 8, 9, 10, 11, 17, 23]
primeCount(primeLst)


#5
#Return number in list that is closest in (absolute) value to target number
hwtime += 4

def closestNumber(lst, target):
  absVals = [] #initialize list
  for elem in lst:
    absVals.append(abs(elem - target)) #append absolute difference to list
  return lst[absVals.index(min(absVals))] #return the index of minimum of the abs differences

closestNumber(primeLst, 4)
closestNumber(primeLst, 5)
closestNumber(primeLst, 4.5)

#6
#Find the greatest common divisor between two numbers
hwtime += 5

def gCD(num1, num2):
  if num1 == num2: #edge case
    return num1
  if num2 < num1:
    num1, num2 = num2, num1 #make sure that there is an ordering
  lst = []
  for i in range(1, num2):
    if num1 % i == 0 and num2 % i == 0: #enumerate divisors, return max of list
      lst.append(i)
  return max(lst)

gCD(24, 48)


#7
#Return index of number in list, or -1 if the number does not exist
hwtime += 10

def findNumber(lst, no):
  if no in lst:
    return lst.index(no) #straightforward
  else:
    return -1

findNumber(primeLst, 11)
findNumber(primeLst, 12)


#8
#Given a list of lists, return the sum
hwtime += 10

def sumNestedLists(nestedLst):
  count = 0 #initialize list
  for elem1 in nestedLst:
    if type(elem1) == list: #if the element is another list, recurse over the element
      count += sumNestedLists(elem1)
    else:
      count += elem1 #if not a list, add the element to the count (assuming numeric)
  return count

nestedLst = [[1, 3, 6, 7], [4, 7, 8], [6, 7, 10]]
sumNestedLists(nestedLst)


#9
#Input: Nested list of numbers, return list that has highest sum
hwtime += 8

def highestList(nested):
  lst = []
  for elem in nested:
    lst.append(sum(elem)) #append the sum of each list
  lstindex = lst.index(max(lst)) #find index of highest sum
  return nested[lstindex] #return the list with highest sum using index

highestList(nestedLst)


#10
#Return the average of a list of numbers
hwtime += 1

def avg(lst):
  return sum(lst) / len(lst)

#11a
#Input list of strings, output single string separated by commas
hwtime += 8

def commaString(lst):
  output = ''
  if len(lst) > 1:
    for i in range(len(lst) - 1):
      output += lst[i] + ', ' #append 'string, ' until last string; only if 2+ elements
    output += lst[len(lst) - 1] #append final string without comma
  else:
    output = lst[0] #if list only has 1 element. Assumption that list is nonempty
  return output

stringLst = ['apple', 'banana', 'orange']
commaString(stringLst)


#11b
#Oxford comma for list of strings
hwtime += 12

def oxfordString(lst):
  output = ''
  if len(lst) <= 1: #just return the first elem if one or less elems (assuming nonempty)
    output =lst[0]
  elif len(lst) == 2:
    output = lst[0] + ' and ' + lst[1] #no comma if only two
  else:
    for i in range(len(lst) - 1):
      output += lst[i] + ', ' #add commas for every element except last
    output += 'and ' + lst[len(lst) - 1] #add 'and ' before last elem, append string
  return output


#Bubble Sort function
hwtime += 7

def bubbleSort(lst):
  while lst[0] != min(lst): #Run multiple iterations until minimum of list is at left
    for i in range(len(lst)-1): #run until second to last index since I do (i + 1) assignments
      if lst[i] > lst[i+1]: #if the left element is greater than right, reassign orders
        lst[i], lst[i+1] = lst[i+1], lst[i]
  return lst

bubbleSort(a)



lst2 = [3, 6, 3, 1, 2]

#Merge two sorted lists
#took ~45 minutes due to linkedlists req + misreading of how the inputs are already sorted
hwtime += 45

def mergeSortedLists(lst1, lst2):
  lst3 = []
  while len(lst1) > 0 or len(lst2) > 0: #run if either list is nonempty
    if len(lst1) == 0:
      lst3.append(lst2.pop(0)) #add lst2 elements in order if lst1 empty
    elif len(lst2) == 0:
      lst3.append(lst1.pop(0)) #symmetric as above
    elif lst1[0] <= lst2[0]:
      lst3.append(lst1.pop(0)) #append lower value
    else:
      lst3.append(lst2.pop(0))
  return lst3


mergeSortedLists(sorted(lst1), sorted(lst2))

def mergeSort(lst):
  if len(lst) <= 1:
    return lst
  else:
    sortedFirstHalf = mergeSort(lst[:len(lst) // 2])
    sortedSecondHalf = mergeSort(lst[len(lst) // 2:])
  return mergeSortedLists(sortedFirstHalf, sortedSecondHalf)

trySortingThis = [-8, -5, 3, 15, -20, 12, 0, -5]
mergeSort(trySortingThis)