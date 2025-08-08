# Create dictionary
student = {"name": "Alice", "age": 22, "course": "Math"}
print (student)

# Access method
print (student.get("name"))      #Alice
print (student.get("garde","N/A"))  #N/A

# keys, values, items
print (student.keys())      
print (student.values())
print (student.items())

# Update
student.update({"age":23})
print (student)

# pop and popitem
student.pop("course")
print (student)

student ["grade"] = "A"
student.popitem()
print (student)

#setdefault
student.setdefault("gender","Female")
print (student)

# copy
copy_student = student.copy()
print (copy_student)

# clear 
student.clear()
print (student)

# Delete
del student

# Check if Key exists
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in thisdict:
    print ("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change the "year" to 2018:
thisdict = {"brand":"Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2018
print (thisdict)    