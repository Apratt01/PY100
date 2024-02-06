my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for i in my_list:
    for x in i:
        if x % 2 == 0:
            print(x)