#Q1
my_data = [10, 'Python', True]
print (my_data)

#Q2
colors = ['red', 'green', 'blue', 'yellow']
print (colors[2])

#Q3
fruits = ['apple', 'banana']
fruits.append("cherry")
print (fruits)

#Q4
numbers = [1,2,4,5]
numbers.insert(2, 3)
print(numbers)

#Q5
items = ['pen', 'book', 'eraser', 'pen']
items.remove('pen')
print(items)

#Q6
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
sub_list = alphabet[3:7]
print (sub_list)

#Q7
original = [1, [2,3], 4]
independant_copy = original.copy()
independant_copy[0] = 100
print(original)
print (independant_copy)

#Q8 Wrong  
scores = [88,75,92,60]      # print(sorted(scores))     
scores.sort()               # sorted(scores).reverse()
scores.reverse()            # print(sorted(scores))
print(scores)               
                          
#Q9 Not Attempted
number = [1,2,3,4,5,6,7,8,9,10]
evens_squared = [x**2 for x in number if x % 2 == 0]
print (evens_squared)

#Q10 Not Attempted
matrix = [[1,2,3], [4,5,6], [7,8,9]]
total_sum = 0
for row in matrix:
    total_sum += sum(row)

print (total_sum)    