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

def newtonRaphson(f, start_point, end_point, TOL):
    N = 100
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


#################Secant method######################
def secant(f, start_point, end_point, TOL):
    N = 100
    x_r = end_point
    x_r0 = start_point
    for i in range(0, N):
        x_r1 = (x_r0 * f(x_r) - x_r * f(x_r0)) / (f(x_r) - f(x_r0))
        if abs(x_r1 - x_r) < TOL:
            return "Secant method soln: x = " + str(
                x_r1) + "\nFound root after {0} iterations between the starting point {1} to ending point {2}".format(
                i + 1, start_point, end_point), 1, x_r1
        x_r0 = x_r
        x_r = x_r1

    return "The method failed after {} iterations".format(N), -1, -1


def choice():
    return fast_real(input("Enter starting point: ")), fast_real(input("Enter ending point: ")), fast_real(
        input("Enter tolerance: "))


#################main######################


def main():
    while (True):
        menu = input(
            "Press 1 for Bisection \nPress 2 for Newton Raphson \nPress 3 for Secant method (anything else to exit):\nchoice:  ")
        print()
        if menu == "1":
            flag = -1
            flag2 = -1
            start_point, end_point, TOL = choice()
            if start_point > end_point:
                start_point, end_point = end_point, start_point
            e_p, s_p = round(start_point + 0.1, 4), start_point
            while s_p < end_point:
                if func(s_p) * func(e_p) < 0:
                    message, result, mid = bisect(func, s_p, e_p, TOL)
                    if result == 1:
                        flag = 1
                        print()
                        print(message)
                        print()
                if funcd(s_p) * funcd(e_p) <= 0:
                    message, result, mid = bisect(funcd, s_p, e_p, TOL)
                    if result == 1:
                        if func(mid) == 0:
                            flag2 = 1
                            print()
                            print("The result came from the derivative:\n" + message)
                            print()
                e_p = round(e_p + 0.1, 4)
                if e_p > end_point:
                    e_p = end_point
                s_p = round(s_p + 0.1, 4)
            if flag == -1 and flag2 == -1:
                print()
                print("No result for each range in size 0.1 between the starting point {0} to ending point {1}".format(
                    s_p, e_p))
                print()
        elif menu == "2":
            flag = -1
            flag2 = -1
            start_point, end_point, TOL = choice()
            if start_point > end_point:
                start_point, end_point = end_point, start_point
            e_p, s_p = round(start_point + 0.1, 4), start_point
            while s_p < end_point:
                if func(s_p) * func(e_p) < 0:
                    message, result, mid = newtonRaphson(f, s_p, e_p, TOL)
                    if result == 1:
                        flag = 1
                        print()
                        print(message)
                        print()
                if funcd(s_p) * funcd(e_p) <= 0:
                    message, result, mid = newtonRaphson(f, s_p, e_p, TOL)
                    if result == 1:
                        if func(mid) == 0:
                            flag2 = 1
                            print()
                            print("The result came from the derivative:\n" + message)
                            print()
                e_p = round(e_p + 0.1, 4)
                if e_p > end_point:
                    e_p = end_point
                s_p = round(s_p + 0.1, 4)
            if flag == -1 and flag2 == -1:
                print()
                print("No result for each range in size 0.1 between the starting point {0} to ending point {1}".format(
                    s_p, e_p))
                print()
        elif menu == "3":
            flag = -1
            flag2 = -1
            mid1 = -1
            start_point, end_point, TOL = choice()
            if start_point > end_point:
                start_point, end_point = end_point, start_point
            e_p, s_p = round(start_point + 0.1, 4), start_point
            res = {}
            while s_p < end_point:
                if func(s_p) * func(e_p) <= 0:
                    message, result, mid = secant(func, s_p, e_p, TOL)
                    if result == 1:
                        if mid not in res.keys():
                            res[mid] = message
                            print()
                            print(message)
                            print()
                        flag = 1
                e_p = round(e_p + 0.1, 4)
                if e_p > end_point:
                    e_p = end_point
                s_p = round(s_p + 0.1, 4)
            if flag == -1 and flag2 == -1:
                print()
                print("No result for each range in size 0.1 between the starting point {0} to ending point {1}".format(
                    s_p, e_p))
                print()
        else:
            break


x = sp.symbols('x')
# f = x ** 4 + x ** 3 - 3 * x ** 2
# f = x ** 3 - x - 1
f = x**2 -x
func = lambdify(x, f)
funcd = f.diff(x)
funcd = lambdify(x, funcd)
main()

# f = "x**3-x-1"


# print(bisect(f, start_point, end_point, TOL))
#
# print(newtonRaphson(f, start_point, end_point, 0.001, 100))

# print(secant(f, start_point, end_point, 0.001, 100))
