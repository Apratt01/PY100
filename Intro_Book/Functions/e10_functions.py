def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# prints the 2 arguments that are passed in, and then prints the default
# paramter 2