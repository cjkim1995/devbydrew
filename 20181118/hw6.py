from hw5 import Queue, Stack

def parentheses(string):
  seen = Stack()
  opening = ['(', '[', '{']
  match = {')':'(', ']':'[', '}':'{'}
  if len(string) % 2 != 0:
    return False
  for char in string:
    if char in opening:
      seen.add(char)
    else:
      if seen.size() == 0:
        return False
      else:
        if match[char] != seen.pop():
          return False
  return True

s1 = '([{}])'
s2 = '()[]'
s3 = '([)]'
s4 = '('

def parentheses_test():
  a = parentheses(s1)
  b = parentheses(s2)
  c = parentheses(s3)
  d = parentheses(s4)
  assert a, "s1 failed"
  assert b, "s2 failed"
  assert c, "s3 failed"
  assert d, "s4 failed"
  return 0



if __name__ == '__main__':
  parentheses_test()
  

  print("All tests passed!")