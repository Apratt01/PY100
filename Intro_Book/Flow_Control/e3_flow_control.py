def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

# the output is Producet 2 for the first method call
# the output is Produce not found! for the second, because it is passing in
# an integer as an argument and the case statement is looking for a string
