from lib.Parser import Parser
from math import sin
import numpy as np


class Midpoint:
    def __init__(self, f, h, lowLimit, UpperLimit, x0, y0):
        self.f = f
        self.h = h
        self.lowLimit = lowLimit
        self.UpperLimit = UpperLimit
        self.x0 = x0
        self.y0 = y0

    def iterations(self):

        i = self.lowLimit
        y0 = self.y0

        print("X\t\tY")
        print(f"{round(i,2)}\t\t{round(y0,5)}")
        for i in np.arange(self.lowLimit, self.UpperLimit, self.h):
            f = Parser(self.f,{'x':i,'y':y0} )
            f = Parser(self.f,{ 'x': i+(self.h/2) ,'y': y0 + (self.h/2)*f.getValue()} )
            y1 = y0 + self.h*f.getValue()
            y0 = y1
            print(f"{round(i+self.h,2)}\t\t{round(y1,5)}")


# f = (lambda x, y: y-(x*x)+1)
# md = Midpoint(f, 0.2, 0, 2, 0, 0.5)
# md.iteration()

f = "1 + (y/x)"
md = Midpoint(f, 0.25, 1, 2, 1, 2)
md.iterations()

