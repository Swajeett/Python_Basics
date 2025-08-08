# Python if .... else
#if Statement :
a = 33 
b = 200 
if b > a:
    print ("b is greater than a")

#elif 
a = 33
b = 33
if b > a:
    print ("b is greater than a")
elif a == b :
    print ("a and b are equal")

# Else
a = 200
b = 33
if b > a:
    print ("b is grater than a")
elif a == b :
    print ("a and b are equal")
else:
    print ("a is greater than b")    

# Short hand if....Else
a = 2
b = 330
print("A") if a > b else print ("B")    

# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
    print ("Both conditiond are True")

# Test if a is greater than b, OR if a if greater than c:
a = 200
b = 33
c = 500
if a > b or a >c:
    print ("At least one of the conditions is True")

# Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
    print ("a is NOT greater than b")

# Nested if 
x = 41
if x > 10:
    print ("Above ten,")
    if x > 20:
        print ("and also above 20!")
    esle:
    print ("but not above 20.")  

# The pass satement 
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass satement to avoid getting an error.

a = 33
b = 200

if b > a:
    pass