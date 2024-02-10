a = 1

def my_function():
    print(a)
    a = 2

my_function()



# The variable a is initialized as a global varialbe on line 1. Within the 
# function on line 4 print is called with a. However on line 5 a is reassigned
# as 2. Since the function does not have any parameters, Python thinks that
# a is being initialized within the function and cannot 'see' the global 
# variable. Since a is after the print function, Python will return an error
# variabel refernced before initialized. This is called variable shadowing.

