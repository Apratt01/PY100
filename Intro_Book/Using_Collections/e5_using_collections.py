# Which of the following values can't be used as a key in a dict, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']
{'a': 1, 'b': 2}
range(5)
{1, 4, 9, 16, 25}
3
0.0
frozenset({1, 4, 9, 16, 25})

# ['a', 'b'], {'a': 1, 'b': 2}, and {1, 4, 9, 16, 25}
# because all three are mutable, and mutable objects cannot be keys
