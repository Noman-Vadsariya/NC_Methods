from math import *
import Functions

def  main():
			
	fx = input("Enter the function whose integral you wish to determine :")      
	f  = lambda x: eval(fx)                                                     

	n = int(input('Enter the number of sub-intervals :')); 
	a = float(input('Please provide the lower limit:')); 
	b = float(input('Please provide the upper limit:')); 

	s  = (f(a) + f(b))/2.0
	h = float((b - a)/n) 
		
	for i in range(1,n):
		s = s + f(a + i*h)
	area = s*h   

	print('The Area is :',area)

if __name__ == "__main__":
	main()