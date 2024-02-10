b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# line 4 is reassigns the element inside the original list object when the 
# function is called on line 6. This prints 10, 2, 3s