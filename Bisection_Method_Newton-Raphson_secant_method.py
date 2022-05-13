import math
from math import ceil
from fastnumbers import fast_real
import sympy as sp
from sympy.utilities.lambdify import lambdify


# INPUT: function (func), low guess (a), high guess (b), tolerance (tol),
#        MAX iterations (N)
# CONDITIONS: a < b, f(a)*f(b) < 0
# OUTPUT: value which differs from a root of f(x)=0 by less than 'tol'
def bisect(func, start_point, end_point, tol):
    # switch low and high if low is larger than high
    N = ((math.log(tol / (end_point - start_point), math.e)) / -math.log(2, math.e))
    N = ceil(N)
    s = start_point
    e = end_point
    for i in range(0, N):
        mid = (end_point + start_point) / 2.0
        if func(mid) == 0 or (end_point - start_point) / 2.0 < tol:
            return "bisect method soln: x = " + str(
                mid) + "\nFound root after {0} iterations between the starting point {1} to ending point {2}".format(
                i + 1, s, e), 1, mid
        elif func(start_point) == 0:
            return "bisect method soln: x = " + str(
                start_point) + "\nFound root after {0} iterations between the starting point {1} to ending point {2}".format(
                i + 1, s, e), 1, start_point
        # same sigh
        if func(mid) * func(start_point) < 0:
            end_point = mid
        # diff sign
        else:
            start_point = mid

    return "Method failed after {} iterations".format(N), -1, -1


##############newton raphson######################

def newtonRaphson(f, start_point, end_point, TOL, N):
    x_r = (start_point + end_point) / 2.0
    s = start_point
    e = end_point
    my_f1 = f.diff(x)
    f = lambdify(x, f)
    my_f1 = lambdify(x, my_f1)

    for i in range(1, N):
        x_r1 = x_r - (f(x_r) / my_f1(x_r))
        if start_point < x_r1 < end_point:
            if func(start_point) == 0:
                return "bisect method soln: x = " + str(
                    start_point) + "\nFound root after {0} iterations between the starting point {1} to ending point {2}".format(
                    i, s, e), 1, start_point
            if my_f1(x_r) == 0:
                if f(x_r) == 0:
                    return "Newton Raphson method soln: x = " + str(
                        x_r) + "\nFound root after {0} iterations between the starting point {1} to ending point {2}".format(
                        i, s, e), 1, x_r
            if (x_r1 - x_r) / 2.0 < TOL:
                return "Newton Raphson method soln: x = " + str(
                    x_r1) + "\nFound root after {0} iterations between the starting point {1} to ending point {2}".format(
                    i, s, e), 1, x_r1

        x_r = x_r1
    return "Method failed after {} iterations".format(N), -1, -1