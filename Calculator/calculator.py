from art import logo
import os

def add(a, b):
    return a+b

def substract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

print(logo)
cont = True
num1 = int(input("Enter 1st no.: "))
for symbol in operation:
    print(symbol)
op = input("Pick an operation: ")
num2 = int(input("Enter 2nd no.: "))
ans = operation[op](num1, num2)
print(f"Output: {ans}")

while cont:
    ch = input("Enter 'y' to continue with {ans}, or enter 'n': ")
    if ch == 'y':
        os.system('cls')
        num3 = int(input("Enter no.: "))
        for symbol in operation:
            print(symbol)
        op = input("Pick an operation: ")
        ans = operation[op](num1, num2)
        print(f"Output: {ans}")
    else:
        cont = False
