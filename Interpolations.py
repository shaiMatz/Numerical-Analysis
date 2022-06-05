import math
import MatrixSolver


def createMatrix(matrix, size, val):
    """

    :param matrix: table
    :param size: table's lentgh
    :param val: whitch natrix to make
    :return: the matrix
    """
    if val == 0:
        matrix = [[0 for i in range(size)] for j in range(size)]
    elif val == 1:
        matrix = [[int(i == j) for i in range(size)] for j in range(size)]
    return matrix


def calcDet(matrix):
    """
    Calculates Determinant

    :param matrix: matrix
    :return: the value
    """
    size = len(matrix)
    det = 0
    if size == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    minor = createMatrix(matrix, size - 1, 0)
    for k in range(len(matrix)):
        i, j = 0, 0
        while i < size:
            if i != k:
                minor[j] = matrix[i][1:]
                j += 1
            i += 1
        det += matrix[k][0] * ((-1) ** k) * calcDet(minor)
    return det


def invertMatrix(matrix):
    """

    :param matrix: matrix
    :return: inverted matrix
    """
    determinant = calcDet(matrix)
    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant], matrix[0][0] / determinant]

    inverse = []
    for i in range(len(matrix)):
        inverseRow = []
        for j in range(len(matrix)):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            inverseRow.append(((-1) ** (i + j)) * calcDet(minor))
        inverse.append(inverseRow)
    inverse = list(map(list, zip(*inverse)))
    for i in range(len(inverse)):
        for j in range(len(inverse)):
            inverse[i][j] = inverse[i][j] / determinant
    return inverse


def Mul_matrix(a, b):
    """

    :param a: matrix a
    :param b: matrix b
    :return: result
    """
    temp = [0 for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            temp[i] += a[i][j] * b[j]
    return temp


def Linear_Method(tab, xf):
    """
    Linear Method for interpolation

    :param tab: table of numbers(x,y)
    :param xf: wanted value
    :return: result
    """
    for i in range(len(tab)):
        if tab[i][0] < xf < tab[i + 1][0]:
            return (tab[i][1] - tab[i + 1][1]) / (tab[i][0] - tab[i + 1][0]) * xf + (
                    (tab[i + 1][1] * tab[i][0]) - (tab[i][1] * tab[i + 1][0])) / (tab[i][0] - tab[i + 1][0])


def Polynomial_Method(tab, xf):
    """
    Polynomial Method for interpolation

    :param tab: table of numbers(x,y)
    :param xf: wanted value
    :return: result
    """
    result, b = 0, [tab[i][1] for i in range(len(tab))]
    poly = Mul_matrix(invertMatrix(Polynomial_creation(tab)), b)
    for i in range(len(poly)):
        result += poly[i] * (xf ** i)
    return result


def Lagrange_Method(tab, xf):
    """
    Lagrange's Method for interpolation

    :param tab: table of numbers(x,y)
    :param xf: wanted value
    :return: result
    """
    Sum, temp = 0, 1
    for i in range(len(tab)):
        for j in range(len(tab)):
            if i != j:
                temp *= (xf - tab[j][0]) / ((tab[i][0]) - tab[j][0])
        Sum += temp * tab[i][1]
        temp = 1
    return Sum


def Polynomial_creation(tab):
    """

    :param tab: table of numbers(x,y)
    :return: result
    """
    for i in range(len(tab)):
        tab[i].insert(0, 1)
    return [[tab[i][1] ** j for j in range(len(tab))] for i in range(len(tab))]


def Nevil_Method(tab, xf):
    """
    Nevil's Method for interpolation

    :param tab: table of numbers(x,y)
    :param xf: wanted value
    :return: result
    """
    def Nevil_P(m, n):
        if m == n:
            return tab[m][1]
        else:
            Px = ((xf - tab[m][0]) * Nevil_P(m + 1, n) - (xf - tab[n][0]) * Nevil_P(m, n - 1)) / (
                    tab[n][0] - tab[m][0])
            return Px

    return Nevil_P(0, len(tab) - 1)


def makeMatrix(m, g):
    """
    Makes a matrix as needed in spline method
    :param m: Array m
    :param g: Array n
    :return: matrix
    """
    matrix = [[0 for i in range(len(m))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            if i == j:
                matrix[i][j] = 2
            elif j == i + 1:
                matrix[i][j] = g[i]
            elif i == j + 1:
                matrix[i][j] = m[i]
    return matrix


def CubicSpline(x, y, wx):
    """

    :param x: Array of x values
    :param y: Array of y values
    :param wx: wanted value
    :return: result
    """
    if wx in x:
        return y[x.index(wx)]
    h = [x[1] - x[0]]
    g = [0]
    m = [0]
    d = [0]
    for i in range(1, len(x)):
        # if i == len(x) - 1:
        #   d.append(0)
        if i != len(x) - 1:
            h.append(x[i + 1] - x[i])
            g.append(h[i] / (h[i - 1] + h[i]))
            d.append((6 / (h[i - 1] + h[i])) * (((y[i + 1] - y[i]) / h[i]) - ((y[i] - y[i - 1]) / h[i - 1])))
            m.append(1 - g[i])
    m.append(0)
    g.append(0)
    d.append(0)
    findX = 0
    for i in range(len(x)):
        if wx < x[i]:
            findX = i - 1
            break
        if i == len(x) - 1:
            findX = len(x) - 2
    matrix = makeMatrix(m, g)
    vec = []
    vec.append(d[findX])
    vec.append(d[findX + 1])
    M = MatrixSolver.matrixSolve(matrix, d)
    return ((((x[findX + 1] - wx) ** 3) * M[findX] + ((wx - x[findX]) ** 3) * M[findX + 1]) / (6 * h[findX])
            + ((x[findX + 1] - wx) * y[findX] + (wx - x[findX]) * y[findX + 1]) / h[findX]
            - (((x[findX + 1] - wx) * M[findX]) + ((wx - x[findX])) * M[findX + 1]) * h[findX] / 6)


def FullCubicSpline(x, y, wx, Y_0, Y_n):
    """

    :param x: Array of x values
    :param y: Array of y values
    :param wx: wanted value
    :return: result
    """
    if wx in x:
        return y[x.index(wx)]
    h = [x[1] - x[0]]
    g = [1]
    m = [0]
    d = [(6 / h[0]) * (((y[1] - y[0]) / h[0]) - Y_0)]
    for i in range(1, len(x)):
        # if i == len(x) - 1:
        #   d.append(0)
        if i != len(x) - 1:
            h.append(x[i + 1] - x[i])
            g.append(h[i] / (h[i - 1] + h[i]))
            d.append((6 / (h[i - 1] + h[i])) * (((y[i + 1] - y[i]) / h[i]) - ((y[i] - y[i - 1]) / h[i - 1])))
            m.append(1 - g[i])
    m.append(1)
    g.append(0)
    d.append((6 / h[len(x) - 2]) * (Y_n - (y[len(x) - 1] - y[len(x) - 2]) / h[0]))
    findX = 0
    for i in range(len(x)):
        if wx < x[i]:
            findX = i - 1
            break
        if i == len(x) - 1:
            findX = len(x) - 2

    matrix = makeMatrix(m, g)
    vec = []
    vec.append(d[findX])
    vec.append(d[findX + 1])
    M = MatrixSolver.matrixSolve(matrix, d)

    # print(d[0])
    # print(d[len(d)-1])
    return ((((x[findX + 1] - wx) ** 3) * M[findX] + ((wx - x[findX]) ** 3) * M[findX + 1]) / (6 * h[findX])
            + ((x[findX + 1] - wx) * y[findX] + (wx - x[findX]) * y[findX + 1]) / h[findX]
            - (((x[findX + 1] - wx) * M[findX]) + ((wx - x[findX])) * M[findX + 1]) * h[findX] / 6)





# TODO Parameters for the interpolation functions, change them by choice!
xList = [1, 2, 3, 4, 5]
yList = [1, 2, 1, 1.5, 1]
x = 1.5
# Parameters only for full spline cubic
ftagzero = 0
ftagn = 1


def main(xList, yList, x):
    matrix1 = []
    matrix2 = []
    matrix3 = []
    matrix4 = []
    matrix5 = []
    matrix6 = []
    for i in range(len(xList)):
        matrix1.append([xList[i], yList[i]])
        matrix2.append([xList[i], yList[i]])
        matrix3.append([xList[i], yList[i]])
        matrix4.append([xList[i], yList[i]])
        matrix5.append([xList[i], yList[i]])
        matrix6.append([xList[i], yList[i]])

    print("Linear Method:\n" + str(Linear_Method(matrix1, x)) + "\n")
    print("Polynomial Method:\n" + str(Polynomial_Method(matrix2, x)) + "\n")
    print("Lagrange Method:\n" + str(Lagrange_Method(matrix3, x)) + "\n")
    print("Nevil Method:\n" + str(Nevil_Method(matrix4, x)) + "\n")
    print("Cubic Spline:\n" + str(CubicSpline(xList, yList, x)) + "\n")
    print("Full Cubic Spline:\n" + str(FullCubicSpline(xList, yList, x, ftagzero, ftagn)) + "\n")


# main
main(xList, yList, x)
