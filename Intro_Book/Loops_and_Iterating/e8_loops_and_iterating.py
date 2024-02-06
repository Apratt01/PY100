my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

# { key: value for element in iterable if condition }

my_dict = { i: len(i) for i in my_set if len(i) % 2 != 0 }
print(my_dict)