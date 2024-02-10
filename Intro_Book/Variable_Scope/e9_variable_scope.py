a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# prints 7, b is bound to 7 when a was passed in as an argument. Since integers
# are not mutable, a was not changed by this reassignement.