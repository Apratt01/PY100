def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# say is a function
# print, input, and max is a built-in function
# upper & lower are methods
