fruits = ['apple', 'banana', 'cherry']

#1. append() - Adds an item to the end
fruits.append('orange')
print ("append:",fruits)

#2  clear() - Removes all elements
fruits.clear()
print("clear:",fruits)

# Re-initialize list
fruits = ['apple', 'banana', 'cherry', 'apple']

#3 copy() - Returns a shallow copy
copied_fruits = fruits.copy()
print ("copy:",copied_fruits)

#4 count() - Returns the count of a specified item
print ("count 'apple':",fruits.count('apple'))

#5 extend() - Adds elements from another iterable 
fruits.extend (['kiwi','mango'])
print ("extend:", fruits) 

#6 index() - Returns the index of the first matched item
print ("index of 'banana':", fruits.index('banana'))

#7 isert() - Inserts an item at a given position 
fruits.insert (1, 'grape')
print ("insert at index 1:", fruits)

#8 pop() _ Removes and returns the item at the given index
popped_item = fruits.pop(2)
print ("pop index 2:", popped_item, "List:",fruits)

#9 remove() - Remove the first occurence of the item 
fruits.remove('apple')
print ("remove 'apple':",fruits)

# 10. reverse() - Reverses the list in place
fruits.reverse()
print("reverse:", fruits)

# 11. sort() - Sorts the list
fruits.sort()
print ("sort:", fruits)
      

