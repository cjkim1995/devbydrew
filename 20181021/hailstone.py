def hailstone(n):
  count = 0
  print(n)
  while n != 1:
    if n % 2 == 0:
      n = n // 2
      count += 1
    else:
      n = 3 * n + 1
      count += 1
    print(n)
  count += 1
  return count

a = hailstone(10)
print(a)


def oneToFifty():
  for i in range(1,51):
    if i % 2 == 0:
      print(i)

oneToFifty()