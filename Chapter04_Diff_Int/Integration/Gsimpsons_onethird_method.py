from math import *
import numpy as np
from sympy import *

class OneThird:
	def __init__(self, f, a, b):
		self.f = f
		self.a = a
		self.b = b

	def iterations(self):
		
		fa = sympify(self.f).subs('x',self.a).evalf()
		fb = sympify(self.f).subs('x',self.b).evalf()
		s  = fa - fb
		h = float((b - a)/n) 

		print(f"Interval (h): {h}")

		print("\nX\t\tY")
		print(f"{a}\t\t{round(fa,7)}")

		for i in range(1,(n-1),2):

			fa = sympify(self.f).subs('x',self.a + i*h).evalf()
			fa_h = sympify(self.f).subs('x',self.a + (i + 1)*h).evalf()

			print(f"{self.a + i*h}\t\t{round(fa,7)}")
			print(f"{self.a + (i + 1)*h}\t\t{round(fa_h,7)}")

			s = s + 4*fa + 2*fa_h
		
		print(f"{b}\t\t{round(fb,7)}")

		area = s*(h/3)   
		print('Area Under the Curve :',area)

if __name__ == "__main__":
	
	f = input("Function : ")                                                           
	f = f.replace("^","**")

	n = int(input('Total Sub-Intervals :')); 
	a = float(input('Lower Limit : ')); 
	b = float(input('Upper Limit : ')); 

	obj = OneThird(f, a, b)
	obj.iterations()