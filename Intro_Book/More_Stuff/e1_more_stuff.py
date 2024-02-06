def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))


# 1 We first call dictionary.keys to get a list of all the keys for the dictionary object.
# 2 Next, we then use composition to call sorted on the list of keys to get a 
#   sorted **list** of the keys in the dictionary object.
# 3 We then use chaining to get the sorted dictionary key at index position 1.
# 4 Finally, we call the upper method on the the key at index position 1.

