from math import *


def next(a, b, equation):

    x = b
    p = eval(equation)
    x = a
    q = eval(equation)

    # Regular falsi method: x = a*f(b)-b*f(a)/f(b)-f(a)
    return (a*p - b*q)/(p-q)


def main():
	# Input Format: x^2+4*x-2:
	equation = input('f(x): ')
	# Handling equation for eval()
	equation = equation.replace("^", "**")

	a = input('Lower Limit: ')
	b = input('Upper limit: ')
	a = float(a)
	b = float(b)
	x = next(a, b, equation)

	while abs(b-a) > 0.00001:  # Corrected upto 10^-6
		if(eval(equation) > 0):
			b = x
		else:
			a = x
		x = next(a, b, equation)

	print('******** REGULAR FALSI METHOD ********')
	print('Approximated root: ', x)


if __name__ == "__main__":
    main()
