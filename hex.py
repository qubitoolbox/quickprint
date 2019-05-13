#prints the memory address in computer.


def printMaddr(b):
  
  for i in range(b):
    print(hex(id(i)), ' the memory address in decimal is = ', '%d' % (i))
  
