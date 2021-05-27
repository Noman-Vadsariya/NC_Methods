from math import *
import numpy as np

sin = np.sin
cos = np.cos
tan = np.tan
pi  = np.pi
exp = np.exp
ln  = np.log
log = np.log10

class Trapezium:
	def __init__(self, f, a, b):
		self.f = f
		self.a = a
		self.b = b
	def iterations(self):
		s  = (f(a) + f(b))/2.0
		h = float((b - a)/n) 
			
		for i in range(1,n):
			s = s + f(a + i*h)
		area = s*h   
		print('The Area is :',area)
     		
if __name__ == "__main__":
	# Input Format: 3*x+2:
	fx = input("Enter the function whose integral you wish to determine :")      
	f  = lambda x: eval(fx)                                                     

	n = int(input('Enter the number of sub-intervals :')); 
	a = float(input('Please provide the lower limit:')); 
	b = float(input('Please provide the upper limit:')); 

	obj = Trapezium(f, a, b)
	obj.iterations()