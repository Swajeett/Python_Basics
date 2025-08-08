# Initial sets
a = {1,2,3,4}
b = {3,4,5,6}
print ("Initial sets:")
print ("a:", a)
print ("b:", b)

# --------- Add, Update ----------

a.add(10)
a.update ([20,30])
print ("\nAfter add and update")
print ("a:", a)

#----------- Remove, Discard, Pop ---------

a.remove (1)
a.discard (999)
removed_item = a.pop()
print ("\nAfter remove, discard, pop:")
print ("a:", a)
print ("Popped item:", removed_item)

#----------- Copy -------------
copy_a = a.copy()
print ("\nCopy of a:", copy_a)

#--------- Clear ------------

temp_set = {100,200}
temp_set.clear()
print ("After clear:", temp_set)

#---------- Set Operations --------------

print ("\nSet operations with a and b:")
print ("Union:", a.union(b))
print ("Intersection:", a.intersection(b))
print ("Difference (a-b):", a.difference(b))
print ("Symmetric Difference:", a.symmetric_difference(b))

# ------------- Comparison ---------

print ("\nSet comparisons:")
print ("Is disjoint:", a.isdisjoint(b))
print ("Is subset (a ⊆ b):", a.issubset(b))
print ("Is superset (a ⊇ b):", a.issuperset(b))

# ------------- In-place Operations ------------
# Reset a to original values
a = {1,2,3,4}
b = {3,4,5,6}

a.intersection_update(b)
print ("\nAfter intersection_update:", a)   # a becomes {3,4}

a = {1,2,3,4}
a.difference_update(b)
print ("After difference_update:", a)   # a becomes {1,2}

a = {1,2,3,4}
a.symmetric_difference_update(b)
print ("After symmetric_difference_update:", a)  # a becomes {1,2,5,6}

a = {1,2}
a.update (b)
print ("After update (union):", a)   # a becomes {1,2,3,4,5,6}