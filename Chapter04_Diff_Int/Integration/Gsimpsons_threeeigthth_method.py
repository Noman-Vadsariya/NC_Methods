from math import *


fx = input("f(x) : ")      
f  = lambda x: eval(fx)                                                      

n = int(input('Enter the number of sub-intervals :'))

if n % 3 == 0:
	print("OKAY ! Wait")
else:
	print("ERROR! No. of sub-intervals should be multiple of 2")
	n = int(input("Enter the new no. of sub-intervals:"))

a = float(input('Lower limit:')); 
b = float(input('Upper limit:')); 

s = f(a) + f(b)
h  = float((b - a)/n)

for i in range(1,(n-1)):
	s = s + 3*f(a + i*h)

for j in range(3,(n-3),3):
	s = s - 3*f(a + j*h)

for k in range(3,(n-3),3):
	s = s + 2*f(a + k*h)


area = (s)*((3*h)/8)   

print('The solution is :',area)