# def createMatrix(matrix, size, val):
#     if val == 0:
#         matrix = [[0 for i in range(size)] for j in range(size)]
#     elif val == 1:
#         matrix = [[int(i == j) for i in range(size)] for j in range(size)]
#     return matrix
#
#
# def calcDet(matrix):
#     size = len(matrix)
#     det = 0
#     if size == 2:
#         det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
#         return det
#     minor = createMatrix(matrix, size - 1, 0)
#     for k in range(len(matrix)):
#         i, j = 0, 0
#         while i < size:
#             if i != k:
#                 minor[j] = matrix[i][1:]
#                 j += 1
#             i += 1
#         det += matrix[k][0] * ((-1) ** k) * calcDet(minor)
#     return det
#
#
# def invertMatrix(matrix):
#     determinant = calcDet(matrix)
#     if len(matrix) == 2:
#         return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
#                 [-1 * matrix[1][0] / determinant], matrix[0][0] / determinant]
#
#     inverse = []
#     for i in range(len(matrix)):
#         inverseRow = []
#         for j in range(len(matrix)):
#             minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
#             inverseRow.append(((-1) ** (i + j)) * calcDet(minor))
#         inverse.append(inverseRow)
#     inverse = list(map(list, zip(*inverse)))
#     for i in range(len(inverse)):
#         for j in range(len(inverse)):
#             inverse[i][j] = inverse[i][j] / determinant
#     return inverse
#
#
# def Mul_matrix(a, b):
#     temp = [0 for i in range(len(a))]
#     for i in range(len(a)):
#         for j in range(len(a)):
#             temp[i] += a[i][j] * b[j]
#     return temp
#
#
# def Linear_Method(tab, xf):
#     for i in range(len(tab)):
#         if tab[i][0] < xf < tab[i + 1][0]:
#             return (tab[i][1] - tab[i + 1][1]) / (tab[i][0] - tab[i + 1][0]) * xf + (
#                     (tab[i + 1][1] * tab[i][0]) - (tab[i][1] * tab[i + 1][0])) / (tab[i][0] - tab[i + 1][0])
#
#
# def Polynomial_Method(tab, xf):
#     result, b = 0, [tab[i][1] for i in range(len(tab))]
#     poly = Mul_matrix(invertMatrix(Polynomial_creation(tab)), b)
#     for i in range(len(poly)):
#         result += poly[i] * (xf ** i)
#     return result
#
#
# def Lagrange_Method(tab, xf):
#     Sum, temp = 0, 1
#     print(tab)
#     for i in range(len(tab)):
#         for j in range(len(tab)):
#             if i != j:
#                 temp *= (xf - tab[j][0]) / ((tab[i][0]) - tab[j][0])
#         Sum += temp * tab[i][1]
#         temp = 1
#     return Sum
#
#
# def Polynomial_creation(tab):
#     for i in range(len(tab)):
#         tab[i].insert(0, 1)
#     return [[tab[i][1] ** j for j in range(len(tab))] for i in range(len(tab))]
#
#
# def Nevil_Method(tab, xf):
#     def Nevil_P(m, n):
#         if m == n:
#             return tab[m][1]
#         else:
#             Px = ((xf - tab[m][0]) * Nevil_P(m + 1, n) - (xf - tab[n][0]) * Nevil_P(m, n - 1)) / (
#                     tab[n][0] - tab[m][0])
#             return Px
#
#     return Nevil_P(0, len(tab) - 1)
#
#
# def driver():
#     print("How many points do you want to enter ?")
#     count = int(input())
#     tab = [[0 for i in range(2)] for j in range(count)]
#     tab1 = [[0 for i in range(2)] for j in range(count)]
#     tab2 = [[0 for i in range(2)] for j in range(count)]
#     tab3 = [[0 for i in range(2)] for j in range(count)]
#     print(tab)
#     for n in range(count):
#         print("x{0}= ".format(n))
#         tab[n][0] = float(input())
#         tab1[n][0] = tab[n][0]
#         tab2[n][0] = tab[n][0]
#         tab3[n][0] = tab[n][0]
#         print("y{0}= ".format(n))
#         tab[n][1] = float(input())
#         tab1[n][1] = tab[n][1]
#         tab2[n][1] = tab[n][1]
#         tab3[n][1] = tab[n][1]
#     print(tab)
#     print("Which point you want to know ?")
#     xf = float(input())
#     # choice = 5
#     # while choice > 4 or choice < 1:
#     #print("Which method you want to use ?\n1.Linear\n2.Polynomial\n3.Lagrange\n4.Nevil")
#     # choice = int(input())
#     # if choice == 1:
#     print("Result = {}".format(Linear_Method(tab, xf)))
#     # if choice == 2:
#     print("Result = {}".format(Polynomial_Method(tab1, xf)))
#     # if choice == 3:
#     print("Result = {}".format(Lagrange_Method(tab2, xf)))
#     # if choice == 4:
#     print("Result = {}".format(Nevil_Method(tab3, xf)))
#
#
# driver()
import math


def CubicSpline(x,y,wx):
    h = []
    g = []
    m = []
    d = []
    for i in range(len(x)):
        if i == len(x) - 1:
            d.append(0)
        if i == 0:
            h.append(x[1]-x[0])
            g.append(0)
            d.append(0)
        else:
            if i != len(x) - 1:
                h.append(x[i + 1] - x[i])
                d.append((6/(h[i-1] + h[i]))*(((y[i+1] - y[i])/h[i])-((y[i] - y[i-1])/h[i-1])))
                g.append(h[i] / (h[i - 1] + h[i]))
                m.append(1-g[i])

    return m,g


def makeMatrix(m,g):
    matrix = [[0 for i in range(len(m))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            if i == j:
                matrix[i][j] = 2
            elif j == i+1:
                matrix[i][j] = g[i]
            elif i == j+1:
                matrix[i][j] = m[i]
    return matrix






m,g = CubicSpline([0,math.pi/6,math.pi/4,math.pi/2],[0,0.5,0.7072,1],math.pi/3)
print(makeMatrix(m,g))

