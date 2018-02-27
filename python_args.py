#!/usr/bin/python

def add(var1, var2):
    return var1 + var2


def sub(var1, var2):
    return var1 - var2


def mul(var1, var2):
    return var1 * var2


def div(var1, var2):
    return var1 / var2


def main():
    ops = str(input("why r u here? = +,-,*,/ :"))
    if ops == '+' or ops == '-' or ops == '*' or ops == '/':
        num1 = int(input("number1? :"))
        num2 = int(input("number2? :"))
        if (ops == '+'):
            print(add(num1, num2))
        elif (ops == '-'):
            print(sub(num1, num2))
        elif (ops == '*'):
            print(mul(num1, num2))
        elif (ops == '/'):
            print(div(num1, num2))
    else:
        # invalid
        print("enter valid")


main()
