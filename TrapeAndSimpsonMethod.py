import math
from math import *

# Input your upper,lower and interval variables


def simpsonsrule(n, upper, lower, h, function):
    rule = 0
    x = lower + h  # Calculates for all odd valures
    for i in range(1, int(n + 1)):
        rule += 4 * function(x)  # adds all calculations to variable rule
        x += 2 * h

    x = lower + 2 * h  # Calculates for all even values
    for i in range(1, int(n)):
        rule += 2 * function(x)  # adds all calculations to variable rule
        x += 2 * h
    ans = (h / 3) * (function(lower) + function(upper) + rule)  # This is carrying out the formula
    return (ans)


def trapeRule(n, upper, lower, intervals, h, function):
    rule = 0
    x = lower
    rule += function(x)  # adds lower value to rule
    x = upper
    rule += function(x)  # adds upper value to rule
    for i in range(1, int(intervals)):  # all values inbetween
        x = lower + h * i
        rule += 2 * (function(x))  # adds these to the rule
    ans = (h / 2) * rule  # completes the function
    return (ans)


def useSimpson(n, upper, lower, h, func, err=0.000001):
    n = int(n)
    if n % 2 == 1:
        n += 1
    res1 = simpsonsrule(n, upper, lower, h, func)
    n2 = n*2
    res2 = simpsonsrule(n2, upper, lower, h, func)
    while abs(res2 - res1) >= err:
        n2 *= 2
        res1 = res2
        res2 = simpsonsrule(n, upper, lower, h, func)
    return res2


def useTrapez(n, upper, lower, h, func, intervals, err=0.000001):
    n = int(n)
    res1 = trapeRule(n, upper, lower, intervals, h, func)
    n *= 2
    res2 = trapeRule(n, upper, lower, intervals, h, func)
    while abs(res2 - res1) >= err:
        n *= 2
        res1 = res2
        res2 = trapeRule(n, upper, lower, intervals, h, func)
    return res2


def f(x):
    f = x**2 - cos(2*x + 1)
    return (f)


def main():
    upper = 3.5
    lower = 1
    n = 4
    z = n / 2  # The number of even functions(z+1 is the number of odd functions)
    ans = 0
    h = (upper - lower) / n
    print("Trapez: ", useTrapez(n, upper, lower, h,f ,n))
    print("Simpson: ", useSimpson(z, upper, lower, h, f))


main()
