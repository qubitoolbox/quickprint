
#Iterator that will print N values, given the iterator, 
#it prints a binary value with its given decimal value.

for i in range(699):
  if not i % 10 == 0:
    print(bin(i), ' = ' , '%d' % (i))
    
