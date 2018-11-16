def sum_to_n(n):
  """
  Problem 5.
  """
  if n <= 1:
    return n
  return n + sum_to_n(n - 1)  

def is_palindrome(s):
  """
  Problem 6.
  """
  if len(s) <= 1:
    return True
  if s[0] != s[-1]:
    return False
  return is_palindrome(s[1:-1])

def my_pow(x, y):
  """
  Problem 7.
  """
  if y == 0:
    if x == 0:
      raise ValueError('0^0 is undefined.')
    return 1
  elif x == 0:
    return 0
  
  if y < 0:
    return 1.0 / my_pow(x, -1 * y)
  square_root = my_pow(x, y // 2)
  if y % 2 == 1:
    return x * square_root * square_root
  return square_root * square_root  

def count_x(s):
  """
  Problem 8.
  """
  if len(s) == 0:
    return 0
  if s[0] == 'x':
    return 1 + count_x(s[1:])
  return count_x(s[1:])   

def contains_six(lst, index):
  """
  Problem 9.
  """
  if index == len(lst):
    return False
  if lst[index] == 6:
    return True
  return contains_six(lst, index + 1)

def clean_string(s):
  """
  Problem 10a.
  """
  if len(s) <= 1:
    return s
  if s[0] == s[1]:
    return clean_string(s[1:])
  return s[0] + clean_string(s[1:])

def remove_duplicate_chars(s):
  """
  Problem 10b.
  """
  return remove_duplicate_chars_helper(s, set())

def remove_duplicate_chars_helper(s, seen_chars):
  if len(s) == 0:
    return ''
  if s[0] not in seen_chars:
    seen_chars.add(s[0])
    return s[0] + remove_duplicate_chars_helper(s[1:], seen_chars)
  return remove_duplicate_chars_helper(s[1:], seen_chars)