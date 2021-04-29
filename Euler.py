# import parser
from math import sin
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
        print()
        for i in np.arange(self.lowLimit, self.UpperLimit+self.h, self.h):
            y1 = y0 + self.h*f(i, y0)
            print(f"{round(i,2)}\t\t{round(y1,5)}")
            y0 = y1


f = (lambda x, y: y-(x*x)+1)
E = Euler(f, 0.2, 0, 2, 0, 0.5)
E.iteration()

# formula = "x**2+x**3"
# code = parser.expr(formula).compile()
# x = 10
# print(eval(code))
