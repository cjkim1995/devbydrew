class Account:
  """A bank account that has a non-negative balance."""
  interest = 0.02
  def __init__(self, account_holder):
    self.balance = 0
    self.holder = account_holder
  def deposit(self, amount):
    """Increase the account balance by amount and return the new balance."""
    self.balance = self.balance + amount
    return self.balance
  def withdraw(self, amount):
    """Decrease the account balance by amount and return the new balance."""
    if amount > self.balance:
      return 'Insufficient funds'
    self.balance = self.balance - amount
    return self.balance


class CheckingAccount(Account):
  """A bank account that charges for withdrawals."""
  withdraw_charge = 1
  interest = 0.01
  def withdraw(self, amount):
    return Account.withdraw(self, amount + self.withdraw_charge)


class TreeNode:
  """Binary search tree class"""
  def __init__(self, item, left = None, right = None):
    self.item = item
    self.left = left
    self.right = right

  def insert(self, item):
    if item < self.item:
      if self.left == None:
        self.left = TreeNode(item)
      else:
        self.left.insert(item)
    else:
      if self.right == None:
        self.right = TreeNode(item)
      else:
        self.right.insert(item)

  # def pSearch(self):
  #   if self.left == None:
  #     print(self.item)
  #     if self.right != None:
  #       self.right.pSearch()
  #   else:
  #     self.left.pSearch()
  #     print(self.item)
  #     self.right.pSearch()
  def traverseIO(self):
    if self.left:
      self.left.traverseIO()
    print(self.item)
    if self.right:
      self.right.traverseIO()






class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert_i(self, item):
    #some code
    # curr = self.root
    # while curr:
    #   prev = curr
    #   if curr.item == item:
    #     return curr #actually incorrect. It has to emcompass if you insert a duplicate, on the right child of the dupe
    #   elif item < curr.item:
    #     curr = curr.left
    #   else:
    #     curr = curr.right

    if self.find(item).item > item:
      self.find(item).left = TreeNode(item)
    elif self.find(item).item < item:
      self.find(item).right = TreeNode(item)
    else:
      self.find(item).right.left = TreeNode(item)

  def insert_r(self, item):
    if self.root == None:
      self.root == TreeNode(item)
      return
    else:
      return self.root.insert(item)



  def find(self, item):
    #return the node containing the item, or the node that should contain the child that would be the item
    prev = self.root
    curr = self.root
    while curr:
      prev = curr
      if curr.item == item:
        return curr #actually incorrect. It has to emcompass if you insert a duplicate
      elif item < curr.item:
        curr = curr.left
      else:
        curr = curr.right

    return prev

  def remove(self, item):
    #some code here
    return None


tree = BinarySearchTree()
tree.root = TreeNode(10)
tree.root.left = TreeNode(5)
tree.root.right = TreeNode(16)
tree.root.right.right = TreeNode(17)

tree1 = BinarySearchTree()
tree1.root = TreeNode(6)
tree1.root.left = TreeNode(3)
tree1.root.left.left = TreeNode(0)
tree1.root.left.right = TreeNode(4)
tree1.root.right = TreeNode(9)
