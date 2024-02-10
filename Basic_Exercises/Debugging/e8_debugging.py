sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = 5
print(matrix) # [['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]