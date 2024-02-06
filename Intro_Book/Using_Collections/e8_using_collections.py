text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8 
print(text.rfind('f', 21, 35))    # 29

print(text[21:35])
print(len(text))

# On line 3 text[21:35] is a new object that contains the value 'for the fjords'
# within that new value, searching for the letter f starting from the right
# returns index 8 from the new substring.

# On line 4, rfind is used with a start parameter at 21 and a stop parameter at
# 35. Starting from the right side of the string and going in, the first 'f'
# from the right starting at index 34, is index 29 of the string text.