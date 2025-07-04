
# calculator
# 2 digits
# + , -, * ,/
# python (console based)

# 2 variables

num1 = float(input(" Enter first number: "))
# print(type(num1))
op = input("Enter operator (+, -, *, /)")
num2 = float(input("Enter second number: "))
# print(type(num2))
if op == "+":
   result= num1 + num2

elif op == "-":
    result = num1 - num2

elif op == "*":
    result = num1 * num2

elif op == "/":
    result = num1 / num2
else:
    print("Invalid")

print(f"Result: {result}")


