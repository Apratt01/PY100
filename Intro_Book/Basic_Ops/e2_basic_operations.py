num = 4936
one = num % 10

num = num // 10
two = num % 10

num = num // 10
three = num % 10

num = num // 10
four = num % 10

print(f"1. One place is {one}.")
print(f"2. Tens place is {two}.")
print(f"3. Hundreds place is {three}.")
print(f"4. Thousands place is {four}.")