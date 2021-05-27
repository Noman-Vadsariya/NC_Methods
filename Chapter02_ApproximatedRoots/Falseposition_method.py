from math import *
from sympy import Symbol, sympify

class FalsePosition:
	def __init__(self, equation, a, b, tolerance):
		self.equation = equation
		self.a = a
		self.b = b
		self.tolerance = tolerance

	def next(self, a, b, equation):

		x = b
		p = eval(equation)
		x = a
		q = eval(equation)

		# Regular falsi method: x = a*f(b)-b*f(a)/f(b)-f(a)
		return (a*p - b*q)/(p-q)

	def iterations(self):
		x = Symbol('x')
		print("A\tF(A)\tB\tF(B)\tC\tF(C)\tAbsolute error")
		x = self.next(self.a, self.b, self.equation)
		Xo = self.a
		Yo = self.b
		
		while abs(self.b-self.a) > self.tolerance:  # Corrected upto 10^-6
			F_A = float(sympify(self.equation).subs('x',self.a).evalf())
			F_B = float(sympify(self.equation).subs('x',self.b).evalf())
			if(eval(self.equation) > 0):
				Yo = self.b
				self.b = x
			else:
				Xo = self
				self.a = x
			print(f"{round(self.a,2)}\t{round(F_A,2)}\t{round(self.b,2)}\t{round(F_B,2)}\t{round(self.b-self.a,5)}\t")
			x = self.next(self.a, self.b, self.equation)

		print('******** REGULAR FALSI METHOD ********')
		print('Approximated root: ', x)


if __name__ == "__main__":
    # Input Format: x^2+4*x-2:
    equation = input('f(x): ')
    # Handling equation for eval()
    equation = equation.replace("^", "**")

    a = float(input('Lower Limit: '))
    b = float(input('Upper limit: '))
    tolerance = float(input('Input the toleramce level: '))

    obj = FalsePosition(equation, a, b, tolerance)
    obj.iterations()
