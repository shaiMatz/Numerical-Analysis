import math
import sympy as sp
from sympy.utilities.lambdify import lambdify


#
# # globals
# TOL = 0.0001
# start_point = -3
# end_point = 200
# N = 19
#
#
# # give python eqn of the formula using python math syntax
# def f(x):
#     return math.pow(x, 2) + 100  # math.pow(x, 4) +math.pow(x, 3)- 3 * math.pow(x, 2)
#
#
# # INPUT: function (func), low guess (a), high guess (b), tolerance (tol),
# #        MAX iterations (N)
# # CONDITIONS: a < b, f(a)*f(b) < 0
# # OUTPUT: value which differs from a root of f(x)=0 by less than 'tol'
# def bisect(func, low, high, tol, N):
#     # switch low and high if low is larger than high
#     if low > high:
#         low, high = high, low
#     # check if valid input
#     if func(low) * func(high) > 0:
#         print("Check input for low and high guess (f(low) and f(high) must have different signs)")
#
#     lastFuncVal = func(low)
#     for i in range(0, N):
#         mid = (high + low) / 2.0
#         if func(mid) == 0 or (high - low) / 2.0 < tol:
#             return mid, i+1
#         # same sigh
#         if func(mid) * func(low) < 0:
#             high = mid
#         # diff sign
#         else:
#             low = mid
#         lastFuncVal = func(mid)
#     return "Method failed after {} iterations".format(N), -1
#
#
# res, iterations = bisect(f, start_point, end_point, TOL, N)
# print("Bisection method soln: x = ", res)
# if iterations != -1:
#     print("Found root after {} iterations".format(iterations))

##############newton raphson######################

# x = 0sp.symbols('x')
# my_f = x ** 3 + 2 * x + 5
# print("my_func: ", my_f)
# my_f1 = sp.diff(my_f, x)
# print("f' : ", my_f1)
# d1 = sp.diff(my_f1)
# print("f'': ", d1)
#
# f = x ** 3 + 2 * x + 5
# f_prime = f.diff(x)
# print("f : ", f)
# print("f' : ", f_prime)
# f = lambdify(x, f)
# f_prime = lambdify(x, f_prime)
# print("f(1):", f(1))
# print("f'(1):", f_prime(1))


