
#Iterator that will print N values, given the iterator, 
#it prints a binary value with its equivalent in decimal value. 
#Values can be even, odd, divisible by N, etc.

def binIterator(a):
  for i in range(a):
    if not i % 10 == 0:
      print(bin(i), ' = ' , '%d' % (i))

def hexIterator(b):
  for k in range(b):
    if not k % 3 == 0:
      print(hex(i), ' = ' , '%d' % (i))
