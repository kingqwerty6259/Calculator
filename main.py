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
        if num2 == "0":
            print("Division by 0 isn't possible")
            return

    if ('.' in num1):
        num1 = float(num1)


    if('.' in num2):
        num2 = float(num2)

    if(num1 != float(num1)):
        num1 = int(num1)
    if(num2 != float(num2)):
        num2 = int(num2)

    if (equation == "+"):
        print (num1, "+", num2, "=", num1 + num2)
    elif (equation == "-"):
        print (num1, "-", num2, "=", num1 - num2)
    elif (equation == "*"):
        print (num1, "x", num2, "=", num1 * num2)
    elif (equation == "/"):
        print(num1, "/", num2, "=", num1/num2)
    else:
        print("Invalid Response")


while run:
    doMath()
