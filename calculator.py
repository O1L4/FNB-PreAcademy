#calculator.py

print("Multi-Function calculator")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

add = round(num1 + num2, 2)
sub = round(num1 - num2, 2)
mul = round(num1 * num2, 2)

print("\nResults:")
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} ={mul}")

if num2 == 0:
    print("Cannot divide by zero")
else:
    div = round(num1 / num2, 2)
    floordiv = round(num1 // num2, 2)
    mod = round(num1 % num2, 2)
    print(f"{num1} / {num2} = {div}")
    print(f"{num1} // {num2} = {floordiv}")
    print(f"{num1} % {num2} = {mod}")