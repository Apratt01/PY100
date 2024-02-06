def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# will error, the 1st paramter does not have a default, and nothing is passed
# in as an argument