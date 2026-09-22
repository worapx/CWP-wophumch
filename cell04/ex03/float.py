from math import floor

num = float(input('Give me a number: '))
if floor(num) == num:
    print(f"This is an integer.")
else:
    print(f"This is a decimal.")