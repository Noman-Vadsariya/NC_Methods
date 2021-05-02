from math import *


def main():
    #Input Format: x^2+4*x-2:
    equation = input('f(x): ')
    #Handling equation for eval()
    equation = equation.replace("^", "**")

    a = input('Lower Limit: ')
    b = input('Upper limit: ')
    a = float(a)
    b = float(b)

    x = (a+b)/2

    while abs(b-a) > 0.00001: #Corrected upto 10^-6
        if(eval(equation) > 0):
            b = x
        else:
            a = x
        x = (a+b)/2

    print('******** BISECTION METHOD ********')
    print('Approximated root: ', x)


if __name__ == "__main__":
    main()
