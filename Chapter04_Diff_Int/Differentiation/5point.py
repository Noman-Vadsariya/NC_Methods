from sympy import *

class FivePoint:
    
    def __init__(self,x_data,y_data,h):
        self.x_data = x_data
        self.y_data = y_data
        self.diff_data = []
        self.h = h
        self.used_points = None
        self.error_bounds = []
        self.x = symbols('x')
        self.fx = sympify("exp(x / 3) + x**2")
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
                self.diff_data.append(self.FivePoint_Midpoint(i))
            elif (i+4 < len(self.x_data)):
                self.diff_data.append(self.Forward_FivePoint_Endpoint(i))
            else:
                self.diff_data.append(self.Backward_FivePoint_Endpoint(i))

            self.getErrorBound()
        
    def get_Diff_data(self):
        return self.diff_data

    def print_table(self):

        print("\nX\t\tF(y)\t\tF'(y)\n")
        for i in range(len(self.x_data)):
            print(f"{round(self.x_data[i],2)}\t\t{round(self.y_data[i],7)}\t{round(self.diff_data[i],7)}\t{self.error_bounds[i]}")


#Validation Required
#Atleast 5 points required

x = [-3,-2.8,-2.6,-2.4,-2.2,-2]
y = [9.367879,8.233241,7.180351,6.209329,5.320305,4.513417]

f = FivePoint(x, y, 0.2)
f.Differentiate()
f.print_table()