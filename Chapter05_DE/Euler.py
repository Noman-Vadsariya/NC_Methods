import numpy as np
from sympy import Symbol,sympify

from lib.processor import Processor

p = Processor()

class Euler:
    def __init__(self, f, h, lowLimit, UpperLimit, x0, y0, Diff_Func):
        self.f = f
        self.h = h
        self.lowLimit = lowLimit
        self.UpperLimit = UpperLimit
        self.x0 = x0
        self.y0 = y0
        self.Diff_Func = Diff_Func 

    def iteration(self):

        i = self.lowLimit
        y0 = self.y0

        x = Symbol('x')
        y = Symbol('y')
        p.clearResults()

        Actual = float(sympify(self.Diff_Func).subs('x',i).evalf())
        Absolute_Error = Actual - y0
        Absolute_Error = abs(Absolute_Error)
        p.addResult({
            "Xi": i,
            "Yi": y0,
            "Euler": Actual,
            "Absolute Error": Absolute_Error
        })
        for i in np.arange(self.lowLimit, self.UpperLimit, self.h):

            y1 = y0 + self.h*sympify(self.f).subs([('x',i),('y',y0)]).evalf()
           
            Actual = float(sympify(self.Diff_Func).subs('x',i+self.h).evalf())
            Absolute_Error = Actual - y1
            Absolute_Error = abs(Absolute_Error)
           
            p.addResult({
                "Xi": i + self.h,
                "Yi": y1,
                "Euler": Actual,
                "Absolute Error": Absolute_Error
            })

            y0 = y1

        p.printResults(("Xi", "Yi", "Euler", "Absolute Error"))

if __name__ == "__main__":
    print("Enter Function: ")
    f= input()
    f=f.replace("^","**")
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
    print("Differential Function: ")
    Diff_Func = input()
    Diff_Func = Diff_Func.replace("^", "**")

    print()
    E = Euler(f,h , low, upper, x0, y0,Diff_Func)
    E.iteration()