def find_integers(tuple_of_numbers):
    result = []
    for i in tuple_of_numbers:
        if type(i) is int:
            result.append(i)
            
    return result


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

integers = find_integers(my_tuple)

print(integers)                    # [1, 3, -4]

