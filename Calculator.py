def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero!"
    return n1 / n2

print("Select the operation you want to perform : +, -, *, /")
operator = input("Enter the operator : ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print("Addition of the two numbers is : ", addition(num1, num2))
    elif operator == '-':
        print("Subtraction of the two numbers is:", subtraction(num1, num2))
    elif operator == '*':
        print("Multiplication of the two numbers is:", multiplication(num1, num2))
    elif operator == '/':
        print("Division of the two numbers is:", division(num1, num2))
    else:
        print("Invalid operator .")
except ValueError:
    print("Please enter valid numbers.")
