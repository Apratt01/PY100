# change the element 'bye' to 'goodbye' in this tuple

stuff = ('hello', 'world', 'bye', 'now') # tuples are immutable
stuff = list(stuff) # since lists aren't immutable, converting to list works
stuff[2] = 'goodbye' # use indexing to make the update
stuff = tuple(stuff) # convert it back to a tuple



print(stuff)