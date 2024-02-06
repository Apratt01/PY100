def capital(str):
    if len(str) > 10:
        return str.upper()
    else:
        return str
        
        
print(capital('hello world'))
print(capital('goodbye'))