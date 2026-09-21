num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
print(f"{num1} x {num2} = {int(num1) * int(num2)}")
if int(num1) * int(num2) > 0:
    print("The result is positive.")
elif int(num1) * int(num2) < 0:
    print("The result is negative.")
else:
    print("The result is zero.")