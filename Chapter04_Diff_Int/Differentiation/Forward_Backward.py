from sympy import *

class Forward_Backward:
    
    def __init__(self,x_data,y_data,h,f):
        self.x_data = x_data
        self.y_data = y_data
        self.diff_data = []
        self.used_points = None
        self.error_bounds = []
        self.absError = []
        self.x = symbols('x')
        self.fx = sympify(f)
        self.diffedFx = None
        self.h = h
        

    def Forward(self,index):
        a = self.y_data[index+1]-self.y_data[index]
        self.used_points = [self.x_data[index + 1], self.x_data[index]]
        return (1/self.h) * a
    
    def Backward(self,index):
        a = self.y_data[index-1]-self.y_data[index]
        self.used_points = [self.x_data[index - 1], self.x_data[index]]
        return (1/-self.h) * a

    def getErrorBound(self):
        w = None
        w = ((self.h / 2) * self.getLargestDerivate())
        self.error_bounds.append(w)

    def setDiffedFunc(self):
        if (self.fx is None):
            return

        self.diffedFx = diff(self.fx, self.x, 2)

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

    def Differentiate(self):

        for i in range(len(self.x_data)):

            if (i+1 < len(self.x_data)):
                self.diff_data.append(self.Forward(i))
            else:
                self.diff_data.append(self.Backward(i))

            self.getErrorBound()
        
        self.getAbsoluteError()
        
    def get_Diff_data(self):
        return self.diff_data

    def print_table(self):
        
        print()
        print('{:<10}{:<16}{:<16}{:<20}{:<20}'.format("X","F(x)","F'(X)","Absolute Error","Error Bound"))
        for i in range(len(self.x_data)):
            print('{:<10}{:<16}{:<16}{:<20}{:<20}'.format(round(self.x_data[i],2),round(self.y_data[i],7),round(self.diff_data[i],7),round(self.absError[i],12),round(self.error_bounds[i],12)))



#Validation Required
#Atleast 2 points required

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
    
    fb = Forward_Backward(x_data, y_data, h,f)
    fb.Differentiate()
    fb.print_table()

# x = [1,1.2,1.4]
# y = [1,1.2625,1.6595]
