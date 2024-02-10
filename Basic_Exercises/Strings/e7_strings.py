def is_empty_or_blank(str):
    return not str or str.isspace()
        
print(is_empty_or_blank('mars'))
print(is_empty_or_blank('  '))
print(is_empty_or_blank(''))