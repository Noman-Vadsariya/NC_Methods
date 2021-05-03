from math import *

class NewtonRaphson:
	def __init__(self, func, func_prime, a, b):
		self.func = func
		self.func_prime = func_prime
		self.a = a
		self.b = b

	def next(self, x, func, func_prime):

		p = eval(func)
		q = eval(func_prime)
		# Newton raphson method: next_x = x - {f(x)/f`(x)}
		return x - (p/q)

	def  iterations(self):
		x = (self.a+self.b)/2
		while True:
			next_x = self.next(x, self.func, self.func_prime)
			if(abs(next_x-x) < 0.00001):
				break
			x = next_x
		
		print('******** NEWTON RAPHSON ********')
		print('Approximated root: ', x)

if __name__ == "__main__":
    # Input Format: x^2+4*x-2:
	func = input('f(x): ')
	# Handling func for eval()
	func = func.replace("^", "**")

	# Input Format: 2x+4
	func_prime = input('First Derivative: ')
	# Handling func for eval()	
	func_prime = func_prime.replace("^","**")

	a = float(input('Lower Limit: '))
	b = float(input('Upper limit: '))

	obj = NewtonRaphson(func,func_prime,a,b)
	obj.iterations()