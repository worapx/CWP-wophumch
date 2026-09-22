num = int(input("Enter a number less than 25: "))
if int(num) >= 25:
    print("Error")
    
while int(num) < 25:
    num += 1
    print(f"Inside the loop, my variable is {num}")
    