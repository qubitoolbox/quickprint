
#Iterator that will print N values, given the iterator, 
#it prints a binary value with its equivalent in decimal value. 
#Values can be even, odd, divisible by N, etc.

for i in range(699):
  if not i % 10 == 0:
    print(bin(i), ' = ' , '%d' % (i))
    
