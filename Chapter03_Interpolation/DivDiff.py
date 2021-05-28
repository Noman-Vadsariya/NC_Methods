import numpy as np
from lib.processor import Processor

pr = Processor()

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

        pr.clearResults()
        pr.addResult({
            "iterative interpolated value": p
        })

        for k in range(1, n + 1):
            p = a[n - k] + (x - self.x_data[n - k])*p
            pr.addResult({
                "iterative interpolated value": p
            })

        pr.printResults(("iterative interpolated value", ))

        pr.clearResults()
        pr.addResult({
            "final interpolated value": p
        })

        pr.printResults(("final interpolated value",))

        return p

    # x_data = [0,0.2,0.4,0.6,0.8]
    # y_data = [1,1.22140,1.49182,1.82212,2.22554]
    #x=0.65