def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return False

def t():
    "*** YOUR CODE HERE ***"
    return 0

def f():
    "*** YOUR CODE HERE ***"
    return 1

with_if_statement()
with_if_function()



def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    nLst = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            nLst.append(n)
        else:
            n *= 3
            n += 1
            nLst.append(n)
    for i in nLst:
        print(i)
    return len(nLst)

a = hailstone(10)
a