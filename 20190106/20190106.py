from math import factorial


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