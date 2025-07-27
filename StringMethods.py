text = "hello world 123"
sample = "HelloWorld"
digits = "12345"
spaces = "   "
identifier = "valid_name"

# 1. count()
print(text.count("l"))  #3

# 2.encode()
print(text.encode())  #b'hello world 123'

# 3. endswith()
print(text.endswith("123")) #True

# 4. expandtabs()
tabbed = "hello\tworld"
print (tabbed.expandtabs(4)) # 'hello world'

# 5. find()
print(text.find("world"))  # 6

# 6. format ()
name = "Alice"
print ("Hello, {}!".format(name)) # Hello, Alice!

#7. format_map ()
print ("coordinates: {x}, {y}".format_map({'x': 10, 'y': 20}))  # Coordinates: 10, 20

# 8. index ()
print (text.index("world")) #6

# 9. isalnum ()
print (sample.isalnum())   # True

# 10. isalpha()
print ("Hello".isalpha())  #True

# 11. isascii()
print("hello123".isascii())  #True

# 12. isdecimal()
print ("123".isdecimal()) #True

# 13. isdigit ()
print (digits.isdigit())  #Ture

# 14. isidentifier ()
print (identifier.isidentifier())  #True

# 15. islower()
print ("hello".islower())  #True

# 16. isnumeric()
print ("123456".isnumeric())  #True

# 17. isprintable()
print ("Hello World!".isprintable())  #True

# 18. isspace ()
print(spaces.isspace())  #True
