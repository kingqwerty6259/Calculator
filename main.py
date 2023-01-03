import math

print("Calculator")
previous = 0
run  = True

def doMath():
    num1 = input("Enter First Number:")
    num2 = input("Enter Second Number:")
    equation = input("Enter Operation Type (Addition/Subtraction/Multiplication/Division):")

    if (equation == "Addition"):
        print (int(num1), "+", int(num2), "=", int(num1)+int(num2))
    elif (equation == "Subtraction"):
        print (int(num1), "-", int(num2), "=", int(num1)-int(num2))
    elif (equation == "Multiplication"):
        print (int(num1), "x", int(num2), "=", int(num1)*int(num2))
    elif (equation == "Division"):
        print (int(num1), "/", int(num2), "=", int(num1)/int(num2))
    else:
        print("Invalid Response")
while run:
    doMath()
