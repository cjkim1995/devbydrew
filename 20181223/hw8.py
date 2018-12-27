#45 minutes
def frequencySort(s):
  """
  Given a string, sort it in decreasing order based on the frequency of characters.
  
  Input: "tree"
  Output: "eert"

  Input:"Aabb"
  Output: "bbaA" or "bbAa"
  """

  assert isinstance(s, str), "Not a string!" #check type for string
  # counts = dict()
  # for i in s:
  #   if i not in counts:
  #     counts[i] = 1
  #   else:
  #     counts[i] += 1
  # ordered_list = []
  # for key in sorted(counts.iteritems(), key = lambda (k, v): v, k):
  #   ordered_list.append(key)
  # for j in ordered_list:

  string_set = set(s) 
  ordered_list = [] #initialize the set of s and an empty list
  for i in string_set:
    ordered_list.append((i, s.count(i))) #iteratively create tuple list, (letter, count)
  ordered_list.sort(key = lambda letter: letter[1], reverse = True) #sort with key, using lambda function. Reverse for descending

  string_to_print = '' #initialize empty string
  for item in ordered_list:
    string_to_print += item[0] * item[1] #iteratively concatenate based on letter * count

  return string_to_print


class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

sll_1 = ListNode(1)
sll_1.next = ListNode(4)
sll_1.next.next = ListNode(5)
sll_2 = ListNode(1)
sll_2.next = ListNode(3)
sll_2.next = ListNode(4)
sll_3 = ListNode(2)
sll_3.next = ListNode(6)
a = [sll_1, sll_2, sll_3]

#def mergeKLists1(lists):
# O(n * k * log(n * k)): n * k to make the new list & make the new linked list, log(n * k) to sort
# iterate over lists {k}
# create a new list, taking the head of every linked list until all lists are empty {n}
# return sorted(new_list) in the form of a linked list {log n * k}


#def mergeKLists2(lists):
# O(n * k * log(k)): n * k to make the new linked list, log(k) to removeMin & insert 
#for list in lists, create a minheap by popping off 0th elements from k lists{k}
#removeMin from heap, create LinkedListNode. Pop off next element from the same list {}
#repeat until heap is None {}




#Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

#35 minutes
def mergeTrees(t1, t2):
  """
  :type t1: TreeNode
  :type t2: TreeNode
  :rtype: TreeNode

  Input: 
  Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
  Output: 
  Merged tree:
       3
      / \
     4   5
    / \   \ 
   5   4   7
  """


  if t1 and t2:
    t3 = TreeNode(t1.val + t2.val)
    if t1.left or t2.left:
      t3.left = mergeTrees(t1.left, t2.left)
    if t1.right or t2.right:
      t3.right = mergeTrees(t1.right, t2.right)
  elif t1 or t2:
    t3 = t1 or t2
  else:
    t3 = None

  return t3

t1, t1.left, t1.left.left, t1.right = TreeNode(1), TreeNode(3), TreeNode(5), TreeNode(2)
t2, t2.left, t2.left.right, t2.right, t2.right.right = TreeNode(2), TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(7)
mergeTrees(t1,t2)


#binary preorder traversal
#15 minutes
def preorderTraversal(root):
  """
  :type root: TreeNode
  :rtype: List[int]
  """
  p_list = []
  if root:
    p_list.append(root.val)
    if root.left:
      p_list.extend(preorderTraversal(root.left))
    if root.right:
      p_list.extend(preorderTraversal(root.right))
  return p_list


#n-ary preorder traversal
# Definition for a Node.
class Node(object):
  def __init__(self, val, children):
    self.val = val
    self.children = children

#45 minutes
def preorder(root):
  """
  :type root: Node
  :rtype: List[int]
  Input:
        1
      / | \
    3   2  4
   / \
  5   6

  Output: [1, 3, 5, 6, 2, 4]
  """

  p_list = []
  if root:
    p_list.append(root.val)
    if root.children:
      for child in root.children:
        p_list.extend(preorder(child))
  return p_list



t4 = Node(1, [Node(3, [Node(5, None), Node(6, None)]), Node(2, None), Node(4, None)])
preorder(t4)

#1 hour
def postorder(root):
  """
  :type root: Node
  :rtype: List[int]
  Input:
        1
      / | \
    3   2  4
   / \
  5   6

  Output: [5, 6, 3, 2, 4, 1]
  """

  p_list = []
  if root:
    if root.children:
      for child in root.children:
          rpo = postorder(child)
          p_list.extend(rpo)
    p_list.extend([root.val])
  return p_list




postorder(t4)



#Merge k sorted python lists
"""
Input: [
[1, 4, 5],
[1, 3, 4],
[2, 6]
]

Output:
[1, 1, 2, 3, 4, 4, 5, 6]
"""

def MergeKPyLsts(lists):
  nlst = []
  rlst = []
  for lst1 in lists:
    for lst2 in lists:
      nlst.append(lst[0])
    min_of_nlst = min(nlst)
    rlst.append(min_of_nlst)
    lst1.pop(min_of_nlst)
  return rlst


