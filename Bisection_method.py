from math import *

def  main():
    #Input Format: x^2+4*x-2: 
	equation = input('f(x): x^2+4*x-2: ')
	equation = equation.replace("^", "**")

	b = input('Upper limit: ')
	a = input('Lower Limit: ')
	b = float(b)
	a = float(a)
 
	x = (a+b)/2

	while abs(b-a) > 0.00001:
		if(eval(equation) > 0) :
			b = x
		else:
			a = x
		x = (a+b)/2
	print('BISECTION METHOD')
	print('Approximated root: ',x)

if __name__ == "__main__":
	main()