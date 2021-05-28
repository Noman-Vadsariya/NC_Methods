from sympy import *
from lib.processor import Processor

p = Processor()

class FivePoint:
    
    def __init__(self,x_data,y_data,h,f):
        self.x_data = x_data
        self.y_data = y_data
        self.diff_data = []
        self.h = h
        self.used_points = None
        self.error_bounds = []
        self.absError = []
        self.x = symbols('x')
        self.fx = sympify(f)
        self.diffedFx = None
        self.isMidpoint = False

    def setDiffedFunc(self):
        if (self.fx is None):
            return

        self.diffedFx = diff(self.fx, self.x, 5)

    def getLargestDerivate(self):
        maxVal = 0
        r = 0

        self.setDiffedFunc()
    
        for xi in self.used_points:
            r = self.diffedFx.subs(self.x, xi)
            if r > maxVal:
                maxVal = r

        return maxVal
    
    def getAbsoluteError(self):
        d = diff(self.fx, self.x, 1)
        
        for i in range(len(self.x_data)):
            Actual = float(d.subs(self.x, self.x_data[i]))
            self.absError.append(abs(Actual-self.diff_data[i]))

    def FivePoint_Midpoint(self,index):
        a = self.y_data[index-2]-8*self.y_data[index-1]+8*self.y_data[index+1]-self.y_data[index+2]
        self.used_points = [self.x_data[index + 1], self.x_data[index - 1], self.x_data[index - 2], self.x_data[index + 2]]
        return (1/(12*self.h)) * a        

    def Forward_FivePoint_Endpoint(self,index):
        a = -25*self.y_data[index]+48*self.y_data[index+1]-36*self.y_data[index+2]+16*self.y_data[index+3]-3*self.y_data[index+4]
        self.used_points = [self.x_data[index + 1], self.x_data[index + 2], self.x_data[index + 3], self.x_data[index + 4], self.x_data[index]]
        return (1/(12*self.h)) * a
    
    def Backward_FivePoint_Endpoint(self,index):
        a = -25*self.y_data[index]+48*self.y_data[index-1]-36*self.y_data[index-2]+16*self.y_data[index-3]-3*self.y_data[index-4]
        self.used_points = [self.x_data[index - 1], self.x_data[index - 2], self.x_data[index - 3], self.x_data[index - 4], self.x_data[index]]
        return (1/(12*-self.h)) * a

    def getErrorBound(self):
        w = None
        if (self.isMidpoint):
            w = (((self.h ** 4) / 30) * self.getLargestDerivate())
        else:
            w = (((self.h ** 4) / 5) * self.getLargestDerivate())

        self.error_bounds.append(w)

    def Differentiate(self):

        for i in range(len(self.x_data)):

            if(i-2 >= 0 and i+2 < len(self.x_data)):
                self.isMidpoint = True
                self.diff_data.append(self.FivePoint_Midpoint(i))
            elif (i+4 < len(self.x_data)):
                self.isMidpoint = False
                self.diff_data.append(self.Forward_FivePoint_Endpoint(i))
            else:
                self.isMidpoint = False
                self.diff_data.append(self.Backward_FivePoint_Endpoint(i))

            self.getErrorBound()
        
        self.getAbsoluteError()

    def get_Diff_data(self):
        return self.diff_data

    def print_table(self):
        p.clearResults()

        for i in range(len(self.x_data)):
            p.addResult({
                "x": self.x_data[i],
                "y": self.y_data[i],
                "y'": self.diff_data[i],
                "absolute error": self.absError[i],
                "error bound": self.error_bounds[i],
            })

        p.printResults(("x", "y", "y'", "absolute error", "error bound"))


#Validation Required
#Atleast 5 points required

if __name__ == "__main__":

    print("Enter No Interpolating Points: ",end="")
    no_points = int(input())

    x_data = []
    y_data = []
    
    print("\nEnter Interpolating Points: ")
    for i in range(0,no_points):
        print(f"x{i} : ",end="")
        x = float(input())
        x_data.append(x)
        print(f"y{i} : ",end="")
        y = float(input())
        y_data.append(y)
        print()

    print("Enter h: ",end="")
    h = float(input())

    print("Enter Function: ",end="")
    f = input()
    f = f.replace("^","**")
    
    f = FivePoint(x_data, y_data, h,f)
    f.Differentiate()
    f.print_table()

# x = [-3,-2.8,-2.6,-2.4,-2.2,-2]
# y = [9.367879,8.233241,7.180351,6.209329,5.320305,4.513417]
# "exp(x / 3) + x**2"