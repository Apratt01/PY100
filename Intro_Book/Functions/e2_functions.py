foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# this prints `bar` because of variable shadowing. Foo is not visible inside
# the funtion