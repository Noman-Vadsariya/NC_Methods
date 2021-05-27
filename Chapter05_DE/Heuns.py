import numpy as np
from math import *
from sympy import Symbol,sympify

class Heuns:
    def __init__(self, f, h, lowLimit, UpperLimit, x0, y0, Diff_Func):
        self.f = f
        self.h = h
        self.lowLimit = lowLimit
        self.UpperLimit = UpperLimit
        self.x0 = x0
        self.y0 = y0
        self.Diff_Func = Diff_Func

    def iterations(self):

        xi = self.lowLimit
        yi = self.y0
        y0 = self.y0

        x = Symbol('x')
        y = Symbol('y')

        print('{:<10}{:<16}{:<16}{:<16}'.format('Xi','Yi',"Heun's","Absolute Error"))
        Actual = float(sympify(self.Diff_Func).subs('x',xi).evalf())
        Absolute_Error = Actual - y0
        Absolute_Error = abs(Absolute_Error)
        print('{:<10}{:<16}{:<16}{:<16}'.format(round(xi,2),round(yi,7),round(Actual,7),round(Absolute_Error,7)))

        for i in np.arange(self.lowLimit, self.UpperLimit, self.h):
        
            k1 = float(sympify(self.f).subs([('x',i),('y',y0)]).evalf())

            k2 = float(sympify(self.f).subs([('x',i + (self.h/3)),('y',y0 + (self.h/3)*k1)]).evalf())
            
            k3 = float(sympify(self.f).subs([('x',i + (2 * self.h/3)),('y',y0 + (2 * self.h/3)*k2)]).evalf())
            
            y1 = y0 + (self.h/4)*(k1+3*k3)

            Actual = float(sympify(self.Diff_Func).subs('x',i+self.h).evalf())
            Absolute_Error = Actual - y1
            Absolute_Error = abs(Absolute_Error)
            print('{:<10}{:<16}{:<16}{:<16}'.format(round(i+self.h,2),round(y1,7),round(Actual,7),round(Absolute_Error,7)))
            y0 = y1

if __name__ == "__main__":
    
    print("Enter Function: ",end= '')
    f= input()
    f = f.replace("^", "**")
    print("Enter Lower Limit: ",end= '')
    low = float(input())
    print("Enter Upper Limit: ",end= '')
    upper = float(input())
    print("Enter h: ",end= '')
    h = float(input())
    print("Enter Initial Conditions: ")
    print("x0 : ",end= '')
    x0 = float(input())
    print("y0 : ",end= '')
    y0 = float(input())
    print()
    print("Differential Function: ")
    Diff_Func = input()
    Diff_Func = Diff_Func.replace("^", "**")

    ME = Heuns(f, h, low, upper,x0 , y0, Diff_Func)
    print()
    ME.iterations()
