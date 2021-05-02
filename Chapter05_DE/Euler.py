from lib.Parser import Parser
import numpy as np


class Euler:
    def __init__(self, f, h, lowLimit, UpperLimit, x0, y0):
        self.f = f
        self.h = h
        self.lowLimit = lowLimit
        self.UpperLimit = UpperLimit
        self.x0 = x0
        self.y0 = y0

    def iteration(self):

        i = self.lowLimit
        y0 = self.y0

        print("X\t\tY")
        print(f"{round(i,2)}\t\t{round(y0,5)}")

        for i in np.arange(self.lowLimit, self.UpperLimit, self.h):
            f = Parser(self.f,{'x':i,'y':y0} )
            y1 = y0 + self.h*f.getValue()
            print(f"{round(i+self.h,2)}\t\t{round(y1,5)}")
            y0 = y1


print("Enter Function: ")
f= input()
print("Enter Lower Limit: ")
low = float(input())
print("Enter Upper Limit: ")
upper = float(input())
print("Enter h: ")
h = float(input())
print("Enter Initial Conditions: ")
print("x0 : ")
x0 = float(input())
print("y0 : ")
y0 = float(input())

print()
E = Euler(f,h , low, upper, x0, y0)
E.iteration()