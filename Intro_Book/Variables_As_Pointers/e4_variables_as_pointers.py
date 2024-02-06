dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1) # dict2 creates a new object that is a copy of dict1
dict1['a'][1] = 42 # since the copy is a shallow copy, nested elements are the same object
print(dict2['a']) 

# the change on line 7 was to a nested list within the dictionary, this change
# is reflected in both dict1 and dict2 becuase dict2 is a shallow copy of dict1