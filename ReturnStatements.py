# return statement = functions send Python values back to the caller
# return statement immediately terminates a function
# return statement can pass an expression back to the caller
# return statement can return multiple values

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    a = int(input("Enter a number: "))
    char = input("Enter an operator: ")
    b = int(input("Enter another number: "))

    if char == "*":
        print(multiply(a, b))
    elif char == "/":
        print(divide(a, b))
    elif char == "+":
        print(add(a, b))
    elif char == "-":
        print(subtract(a, b))
    else:
        print("Invalid operator")

main()
