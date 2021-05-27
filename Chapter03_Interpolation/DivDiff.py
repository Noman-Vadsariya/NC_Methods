import numpy as np

class DividedDifference:

    def __init__(self,x_data,y_data):

        self.x_data = x_data
        self.y_data = y_data
        
    def _poly_newton_coefficient(self,x, y):

        m = len(x)

        x = np.copy(x)
        a = np.copy(y)

        print("\n--------Divided Difference Table--------\n")
        for k in range(1, m):
            a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])

            print(a[k:m])

        return a

    def newton_polynomial(self, x):
        a = self._poly_newton_coefficient(self.x_data, self.y_data)
        n = len(self.x_data) - 1  # Degree of polynomial
        p = a[n]

        for k in range(1, n + 1):
            p = a[n - k] + (x - self.x_data[n - k])*p

        return p


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

    print("Enter Value to be Interpolated: ",end="")
    # x=0.65
    x = float(input())

    Div = DividedDifference(x_data,y_data)
    print(f'\nFinal Interpolated Value : {round(Div.newton_polynomial(0.65),5)}')

    # x_data = [0,0.2,0.4,0.6,0.8]
    # y_data = [1,1.22140,1.49182,1.82212,2.22554]
    #x=0.65