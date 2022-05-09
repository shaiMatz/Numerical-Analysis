import math
from math import ceil

import sympy as sp
from sympy.utilities.lambdify import lambdify


# INPUT: function (func), low guess (a), high guess (b), tolerance (tol),
#        MAX iterations (N)
# CONDITIONS: a < b, f(a)*f(b) < 0
# OUTPUT: value which differs from a root of f(x)=0 by less than 'tol'
def bisect(func, low, high, tol):
    # switch low and high if low is larger than high
    N = ((math.log(tol / (end_point - start_point), math.e)) / -math.log(2, math.e))
    N = ceil(N)

    f = lambdify(x, func)  # if already did lambdify throw exception
    func = f

    if low > high:
        low, high = high, low

    for i in range(0, N):
        mid = (high + low) / 2.0
        if func(mid) == 0 or (high - low) / 2.0 < tol:
            return "bisect method soln: x = " + str(mid) + "\nFound root after {} iterations".format(i + 1), 1
        # same sigh
        if func(mid) * func(low) < 0:
            high = mid
        # diff sign
        else:
            low = mid

    return "Method failed after {} iterations".format(N), -1



##############method######################


# f = "x**3-x-1"
x = sp.symbols('x')
f = 4 * x ** 3 - 48 * x + 5
TOL = 0.001
start_point = 3
end_point = 4
N = 50


print(bisect(f, start_point, end_point, TOL))


