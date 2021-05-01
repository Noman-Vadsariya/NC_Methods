import numpy as np

def _poly_newton_coefficient(x, y):

    m = len(x)

    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])

    return a

def newton_polynomial(x_data, y_data, x):
    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1  # Degree of polynomial
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p

    return p

x = [0,0.2,0.4,0.6,0.8]
y = [1,1.22140,1.49182,1.82212,2.22554]

p = newton_polynomial(x, y,0.65)
print(p)