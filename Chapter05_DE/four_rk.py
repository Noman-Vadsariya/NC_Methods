from re import A
from token import AWAIT
import numpy as np
from math import *
from sympy import Symbol, sympify

from lib.processor import Processor

p = Processor()

class FourthOrder:
    def __init__(self, f, h, lowLimit, UpperLimit, x0, y0,Diff_Func):
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
        p.clearResults()

        # print('{:<10}{:<16}{:<16}{:<16}'.format('Xi','Yi',"Runge-Kutta","Absolute Error"))
        Actual = float(sympify(self.Diff_Func).subs('x',xi).evalf())
        Absolute_Error = Actual - y0
        Absolute_Error = abs(Absolute_Error)
        p.addResult({
            "Xi": xi,
            "Yi": y0,
            "Runge-Kutta": Actual,
            "Absolute Error": Absolute_Error
        })
        # print('{:<10}{:<16}{:<16}{:<16}'.format(round(xi,2),round(y0,7),round(Actual,7),round(Absolute_Error,7)))


        for i in np.arange(self.lowLimit, self.UpperLimit, self.h):
        
            k1 = self.h*sympify(self.f).subs([('x',i),('y',y0)]).evalf()

            k2 = self.h*sympify(self.f).subs([('x',i + (self.h/2)),('y',y0 + (1/2)*k1)]).evalf()
            
            k3 = self.h*sympify(self.f).subs([('x',i + (self.h/2)),('y',y0 + (2 * 1/2)*k2)]).evalf()
            
            k4 = self.h*sympify(self.f).subs([('x',i + self.h),('y',y0 + k3)]).evalf()
            
            y1 = y0 + (1/6)*(k1+2*k2+2*k3+k4)


            #Actual Values and Error Values
            Actual = sympify(self.Diff_Func).subs('x',i+self.h).evalf()
            Absolute_Error = y1 - Actual 
            Absolute_Error = abs(Absolute_Error)

            p.addResult({
                "Xi": (i + self.h),
                "Yi": y1,
                "Runge-Kutta": Actual,
                "Absolute Error": Absolute_Error
            })

            # print('{:<10}{:<16}{:<16}{:<16}'.format(round(i+self.h,2),round(y1,7),round(Actual,7),round(Absolute_Error,7)))
            
            y0 = y1
        
        p.printResults(("Xi", "Yi", "Runge-Kutta", "Absolute Error"))

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
    print("Differential Function: ")
    Diff_Func = input()
    Diff_Func = Diff_Func.replace("^", "**")

    print()
    ME = FourthOrder(f, h, low, upper,x0 , y0,Diff_Func)
    ME.iterations()
