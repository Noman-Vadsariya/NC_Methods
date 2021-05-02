from math import *

def  main():
	fx = input("f(x) : ")      
	f  = lambda x: eval(fx)                                                     
	n = int(input('Enter the number of sub-intervals :'))

	if n % 2 == 0:
		print("OKAY ! Wait")
	else:
		print("ERROR! No. of sub-intervals should be multiple of 2")
		n = int(input("Enter the new no. of sub-intervals:"))

	a = float(input('Lower limit: ')); 
	b = float(input('Upper limit: ')); 

	s  = f(a) - f(b)
	h = float((b - a)/n) 
		
	for i in range(1,(n-1),2):
		s = s + 4*f(a + i*h) + 2*f(a + (i + 1)*h)
	area = s*(h/3)   

	print('The Area is :',area)

if __name__ == "__main__":
	main()