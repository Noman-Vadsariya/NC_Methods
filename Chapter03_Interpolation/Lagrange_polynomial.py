# from math import *
# import numpy as np
# import interpolation
from math import *
import numpy as np
import interpolation
import ode
import solutions

def lagrange(x, y, x_int):
    n = x.size
    y_int = 0

    for i in range(0, n):
        p = y[i]
        for j in range(0, n):
            if i != j:
                p = p * (x_int - x[j]) / (x[i] - x[j])
        y_int = y_int + p

    return [y_int]

def run_example_lagrange():
    print("\n\n[Example] Interpolation: Lagrange")
    x = np.array([2, 11 / 4, 4])
    y = np.array([1 / 2, 4 / 11, 1 / 4])
    x_int = 3
    print_var("x", x)
    print("y", y)
    print("x_int", x_int)
    [y_int] = interpolation.lagrange(x, y, x_int)
    print_var("y_int", y_int)


if __name__ == "__main__":
     run_example_lagrange()