x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# This will error, x is not initialized inside the function. It is not passed
# into the function as an argument. Python doesn't know what to do with it.
# You will get a local variable x is not initialized before assignement.