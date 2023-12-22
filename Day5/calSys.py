import sys

def addition(num1, num2):
    add = num1 + num2
    return add

def subtraction(num1, num2):
    s = num1 - num2
    return s

def multiplication(num1, num2):
    mul = num1 * num2
    return mul

def division(num1, num2):
    dev = num1 / num2
    return dev

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "addition":
    output = addition(num1, num2)
    print(output)
elif operation == "subtraction":
    output = subtraction(num1, num2)
    print(output)
elif operation == "multiplication":
    output = multiplication(num1, num2)
    print(output)
elif operation == "division":
    output = division(num1, num2)
    print(output)
else:
    print("Invalid operation. Please choose addition, subtraction, multiplication, or division.")