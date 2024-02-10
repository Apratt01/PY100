a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# the keyword global tells the function that the variable a refers to the global
# variable a initialized outside of the function. Operations within the function
# will affect the global variable 1 reassigning global a to a new value of 2.
# this will print 2