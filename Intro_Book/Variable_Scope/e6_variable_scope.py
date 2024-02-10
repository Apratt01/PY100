a = 1

def my_function():
    a = 2

my_function()
print(a)

# the function call does not do anything to the global variable initialized
# before the function. The print function will print 1. Variable Shadowing.