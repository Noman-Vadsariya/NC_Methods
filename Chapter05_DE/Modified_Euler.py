from lib.Parser import Parser
import numpy as np

class Modified_Euler:
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
            
            f = Parser(self.f,{'x':i,'y':y0})
            k1 = self.h*f.getValue()
            f = Parser(self.f,{'x':i+self.h,'y':y0+k1})
            k2 = self.h*f.getValue()
            y1 = y0 + 0.5*(k1+k2)

            print(f"{round(i+self.h,2)}\t\t{round(y1,5)}")
            
            y0 = y1

# f = lambda x,y: -2*x*(y*y)
# ME = Modified_Euler(f, 0.1, 0, 0.5, 0, 1)
# ME.iterations()

f ="1 + (y/x)"
ME = Modified_Euler(f, 0.25, 1, 2, 1, 2)
ME.iterations()