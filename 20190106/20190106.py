from math import factorial

def factorize(num):
  facts = []

  while num % 2 == 0:
    facts.append(2)
    num /= 2

  for odd in range(3, int(num ** 0.5) + 1, 2):
    while num % odd == 0:
      facts.append(odd)
      num /= odd

  if num >= 2:
    facts.append(num)

  return facts


def trailing_zeroes(number):
  new_num = factorial(number)
  fcount = 0
  tcount = 0
  while new_num % 5 == 0:
    fcount += 1
    new_num /= 5
  while new_num % 2 == 0:
    tcount += 1
    new_num /= 2

  return min(fcount, tcount)