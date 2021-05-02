from math import *

def next(x, func, func_prime):

	p = eval(func)
	q = eval(func_prime)
	
	# Newton raphson method: next_x = x - {f(x)/f`(x)}
	return x - (p/q)

def  main():

	# Input Format: x^2+4*x-2:
	func = input('f(x): ')
	# Handling func for eval()
	func = func.replace("^", "**")

	# Input Format: 2x+4
	func_prime = input('First Derivative: ')
	# Handling func for eval()	
	func_prime = func_prime.replace("^","**")

	
	a = input('Lower Limit: ')
	b = input('Upper limit: ')
	a = float(a)
	b = float(b)


	
	x = (a+b)/2

	
	while True:
		next_x = next(x, func, func_prime)
		if(abs(next_x-x) < 0.00001):
			break
		x = next_x
	
	print('******** NEWTON RAPHSON ********')
	print('Approximated root: ', x)

if __name__ == "__main__":
	main()