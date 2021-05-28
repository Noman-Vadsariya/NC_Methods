from sympy import *
from lib.processor import Processor

p = Processor()

class ThreePoint:
    
    def __init__(self,x_data,y_data,h,f):
        self.x_data = x_data
        self.y_data = y_data
        self.used_points = None
        self.error_bounds = []
        self.diff_data = []
        self.absError = []
        self.h = h
        self.x = symbols('x')
        self.fx = sympify(f)
        self.diffedFx = None
        self.isMidpoint = False

    def setDiffedFunc(self):
        if (self.fx is None):
            return

        self.diffedFx = diff(self.fx, self.x, 3)

    def getLargestDerivate(self):
        maxVal = 0
        r = 0

        self.setDiffedFunc()
    
        for xi in self.used_points:
            r = self.diffedFx.subs(self.x, xi)
            if r > maxVal:
                maxVal = r

        return maxVal

    def getErrorBound(self):
        w = None
        if (self.isMidpoint):
            w = (((self.h ** 2) / 6) * self.getLargestDerivate())
        else:
            w = (((self.h ** 2) / 3) * self.getLargestDerivate())

        self.error_bounds.append(w)
    
    def getAbsoluteError(self):
        d = diff(self.fx, self.x, 1)
        
        for i in range(len(self.x_data)):
            Actual = float(d.subs(self.x, self.x_data[i]))
            self.absError.append(abs(Actual-self.diff_data[i]))

    def ThreePoint_Midpoint(self,index):
        a = self.y_data[index+1]-self.y_data[index-1]
        self.used_points = [self.x_data[index + 1], self.x_data[index - 1]]
        return (1/(2*self.h)) * a        

    def Forward_ThreePoint_Endpoint(self,index):
        a = -3*self.y_data[index]+4*self.y_data[index+1]-self.y_data[index+2]
        self.used_points = [self.x_data[index + 1], self.x_data[index + 2], self.x_data[index]]
        return (1/(2*self.h)) * a
    
    def Backward_ThreePoint_Endpoint(self,index):
        a = -3*self.y_data[index]+4*self.y_data[index-1]-self.y_data[index-2]
        self.used_points = [self.x_data[index - 1], self.x_data[index - 2], self.x_data[index]]
        return (1/(2*-self.h)) * a

    def Differentiate(self):

        for i in range(len(self.x_data)):

            if(i-1 >= 0 and i+1 < len(self.x_data)):
                self.isMidpoint = True
                self.diff_data.append(self.ThreePoint_Midpoint(i))
            elif (i+2 < len(self.x_data)):
                self.isMidpoint = False
                self.diff_data.append(self.Forward_ThreePoint_Endpoint(i))
            else:
                self.isMidpoint = False
                self.diff_data.append(self.Backward_ThreePoint_Endpoint(i))

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
    
    t = ThreePoint(x_data, y_data, h,f)
    t.Differentiate()
    t.print_table()

#Validation Required
#Atleast 3 points required

# x = [2,2.1,2.2,2.3]
# y = [3.6887983,3.6905701,3.6688192,3.6245909]


# '2*ln(x)**2 + 3*sin(x)'