from math import *
import Functions

fx = input("Enter the function whose integral you wish to determine :")      
f  = lambda x: eval(fx)                                                     


n = int(input('Enter the number of sub-intervals :'))

if n % 2 == 0:
	print("The chosen no. of sub-intervals is good")
else:
	print("ERROR! : The chosen no. of sub-intervals should be a multiple of 2")
	n = int(input("Enter the new no. of sub-intervals:"))

a = float(input('Please provide the lower limit:')); 
b = float(input('Please provide the upper limit:')); 

s  = f(a) - f(b)
h = float((b - a)/n) 
	
for i in range(1,(n-1),2):
	s = s + 4*f(a + i*h) + 2*f(a + (i + 1)*h)
area = s*(h/3)   

print('The solution is :',area)