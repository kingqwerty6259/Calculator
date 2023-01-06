import math

print("Calculator")
previous = 0
run  = True

def doMath():
    num1 = input("Enter First Number:")
    num2 = input("Enter Second Number:")
    equation = input("Enter Operation Type (+,-,*,/):")

    if (len(equation) > 1):
        equation = equation.replace(" ", "")

    if num1.isalpha():
        print("Invalid Input")
        return
    if num2.isalpha():
        print("Invalid Input")
        return
    if equation == "/":
        if num1 == "0":
            return
        elif num2 == "0":
            return


    if (equation == "+"):
        print (int(num1), "+", int(num2), "=", int(num1)+int(num2))
    elif (equation == "-"):
        print (int(num1), "-", int(num2), "=", int(num1)-int(num2))
    elif (equation == "*"):
        print (int(num1), "x", int(num2), "=", int(num1)*int(num2))
    elif (equation == "/"):
        print (int(num1), "/", int(num2), "=", int(num1)/int(num2))
    else:
        print("Invalid Response")


while run:
    doMath()
