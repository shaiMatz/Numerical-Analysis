import math


def f(x):
    f=math.sin(x)
    return (f)


import math as m

def trapezium(n, a, b, func,  ) -> float:
    dx = (b - a)/n
    sum = (func(a) + func(b))/2
    for i in range(1, n, 1):
        sum += func(a + i*dx)
    return sum*dx

def Romberg_interpolation(a, b, N=2 , func = lambda x: (x**2)*(m.e**x), eps=0.0001,  values =[], m=1):
    """a-start point, b-end point"""
    if N<2: N=2
    n = N
    for i in range( len(values) , N ):
        values.extend([[trapezium(n, a, b, func)]])
        for j in range(1, i+1):
            values[i].append((values[i][j-1]*(4**j) - values[i-1][j-1])/(4**j - 1))
        n *= 2
    if abs(values[N-1][N-1]-values[N-2][N-2]) > eps :
        Romberg_interpolation(a, b, N*2, eps=eps, values=values, func=func)
    weizhi=len(values[len(values)-1])#last string length
    return values[len(values)-1][weizhi-1],values


if __name__=="__main__":
    eps=10**(-5)
    a=0
    b=1
    func = lambda x: 1/(2+x**4)
    N=2
    result,value=Romberg_interpolation(a, b, N=N, eps=eps, func=func )
    print("%.7f"%(result))
    for i in range(len(value)):
        print(value[i])
    # for i in range(3):
    #     for j in range(3):
    #         if(i>=j):
    #             print(value[i][j])
#lambda x: (x ** 2) * (m.e ** x)