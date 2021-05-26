from math import *

class FalsePosition:
	def __init__(self, equation, a, b):
		self.equation = equation
		self.a = a
		self.b = b

	def next(self, a, b, equation):

		x = b
		p = eval(equation)
		x = a
		q = eval(equation)

		# Regular falsi method: x = a*f(b)-b*f(a)/f(b)-f(a)
		return (a*p - b*q)/(p-q)

	def iterations(self):
		x = self.next(self.a, self.b, self.equation)

		while abs(self.b-self.a) > 0.00001:  # Corrected upto 10^-6
			if(eval(self.equation) > 0):
				self.b = x
			else:
				self.a = x
				x = self.next(self.a, self.b, self.equation)

		print('******** REGULAR FALSI METHOD ********')
		print('Approximated root: ', x)
