from lib.Parser import Parser
import numpy as np
from math import *

class Heuns:
    def __init__(self, f, h, lowLimit, UpperLimit, x0, y0):
        self.f = f
        self.h = h
        self.lowLimit = lowLimit
        self.UpperLimit = UpperLimit
        self.x0 = x0
        self.y0 = y0

    def iterations(self):

        x = self.lowLimit
        y = self.y0
        y0 = self.y0

        print("X\t\tY")
        print(f"{round(x,2)}\t\t{round(y,7)}")
        for i in np.arange(self.lowLimit, self.UpperLimit, self.h):
        
            k1 = eval(f)

            x = i + (self.h/3)
            y = y0 + (self.h/3)*k1 
            k2 = eval(f)
            
            x = i + (2 * self.h/3)
            y = y0 + (2 * self.h/3)*k2
            k3 = eval(f)
            
            y1 = y0 + (self.h/4)*(k1+3*k3)

            print(f"{round(i+self.h,2)}\t\t{round(y1,7)}")
            
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

    ME = Heuns(f, h, low, upper,x0 , y0)
    ME.iterations()
