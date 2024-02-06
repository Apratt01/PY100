set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1 # points to the same object
set1.add(range(5, 10))
print(set2)

# set1 & set2 reference the same object. When set1 is changed set2 reflects that change