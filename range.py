''' In Python, range() is used to generate a sequence of numbers.
It is most commonly used in loops, especially for loops.

Python range() Basics
Syntax:
range(start,stop,step)
'''

# range(stop) --- starts from 0
for i in range (5):
    print(i)

# range(start,stop)
for i in range (2, 7):
    print(i)

# range(start, stop, step)
# step controls jump between values.
for i in range(1, 10, 2):
    print(i)    

# Reverse Range. Use negative step:
for i in range (10,0,-1):
    print (i) 

# Range converted to list 
list (range(5))


