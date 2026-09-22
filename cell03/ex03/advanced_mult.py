for num in range(11):
    print(f"Table de {num}: ", end="")
    for i in range(1, 11):
        result = num * i
        print(f"{result} ", end="")
    print()