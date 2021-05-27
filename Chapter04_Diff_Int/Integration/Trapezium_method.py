from math import *
import numpy as np
from sympy import Symbol, sympify

class Trapezium:
	def __init__(self, f, a, b):
		self.f = f
		self.a = a
		self.b = b
	
	def iterations(self):

		fa = sympify(self.f).subs('x',self.a).evalf()
		fb = sympify(self.f).subs('x',self.b).evalf()
		s  = (fa + fb)/2.0
		h = float((self.b - self.a)/n) 
		
		print(f"Interval (h): {h}")

		print("\nX\t\tY")
		print(f"{a}\t\t{round(fa,7)}")

		for i in range(1,n):
			
			fa = sympify(self.f).subs('x',self.a + i*h).evalf()
			print(f"{self.a + i*h}\t\t{round(fa,7)}")

			s = s + fa

		print(f"{b}\t\t{fb}\n")

		area = s*h
		print('\nAre Under the Curve :',round(area,7))
     		
if __name__ == "__main__":
	f = input("Function : ")                                                           
	f = f.replace("^","**")

	n = int(input('Total Sub-Intervals :')); 
	a = float(input('Lower Limit : ')); 
	b = float(input('Upper Limit : ')); 

	obj = Trapezium(f, a, b)
	obj.iterations()