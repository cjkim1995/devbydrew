from math import factorial


def trailing_zeroes(number):
  new_num = factorial(number) #factorial of number
  fcount = 0
  tcount = 0 #initialize counts, the number of trailing zeroes is the min of factors of 2 & 5
  while new_num % 5 == 0: #factor out 5s, increment count
    fcount += 1
    new_num /= 5
  while new_num % 2 == 0: #factor out 2s, increment count
    tcount += 1
    new_num /= 2

  return min(fcount, tcount) #return the minimum. If there's 7 factors of 5 and 2 factors of 2, only 2 trailing zeroes


