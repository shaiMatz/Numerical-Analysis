def createMatrix(matrix, size, val):
    if val == 0:
        matrix = [[0 for i in range(size)] for j in range(size)]
    elif val == 1:
        matrix = [[int(i == j) for i in range(size)] for j in range(size)]
    return matrix


def calcDet(matrix):
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
    temp = [0 for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            temp[i] += a[i][j] * b[j]
    return temp


def Linear_Method(tab, xf):
    for i in range(len(tab)):
        if tab[i][0] < xf < tab[i + 1][0]:
            return (tab[i][1] - tab[i + 1][1]) / (tab[i][0] - tab[i + 1][0]) * xf + (
                    (tab[i + 1][1] * tab[i][0]) - (tab[i][1] * tab[i + 1][0])) / (tab[i][0] - tab[i + 1][0])


def Polynomial_Method(tab, xf):
    result, b = 0, [tab[i][1] for i in range(len(tab))]
    poly = Mul_matrix(invertMatrix(Polynomial_creation(tab)), b)
    for i in range(len(poly)):
        result += poly[i] * (xf ** i)
    return result


def Lagrange_Method(tab, xf):
    Sum, temp = 0, 1
    print(tab)
    for i in range(len(tab)):
        for j in range(len(tab)):
            if i != j:
                temp *= (xf - tab[j][0]) / ((tab[i][0]) - tab[j][0])
        Sum += temp * tab[i][1]
        temp = 1
    return Sum


def Polynomial_creation(tab):
    for i in range(len(tab)):
        tab[i].insert(0, 1)
    return [[tab[i][1] ** j for j in range(len(tab))] for i in range(len(tab))]


def Nevil_Method(tab, xf):
    def Nevil_P(m, n):
        if m == n:
            return tab[m][1]
        else:
            Px = ((xf - tab[m][0]) * Nevil_P(m + 1, n) - (xf - tab[n][0]) * Nevil_P(m, n - 1)) / (
                    tab[n][0] - tab[m][0])
            return Px

    return Nevil_P(0, len(tab) - 1)


def driver():
    print("How many points do you want to enter ?")
    count = int(input())
    tab = [[0 for i in range(2)] for j in range(count)]
    tab1 = [[0 for i in range(2)] for j in range(count)]
    tab2 = [[0 for i in range(2)] for j in range(count)]
    tab3 = [[0 for i in range(2)] for j in range(count)]
    print(tab)
    for n in range(count):
        print("x{0}= ".format(n))
        tab[n][0] = float(input())
        tab1[n][0] = tab[n][0]
        tab2[n][0] = tab[n][0]
        tab3[n][0] = tab[n][0]
        print("y{0}= ".format(n))
        tab[n][1] = float(input())
        tab1[n][1] = tab[n][1]
        tab2[n][1] = tab[n][1]
        tab3[n][1] = tab[n][1]
    print(tab)
    print("Which point you want to know ?")
    xf = float(input())
    # choice = 5
    # while choice > 4 or choice < 1:
    #print("Which method you want to use ?\n1.Linear\n2.Polynomial\n3.Lagrange\n4.Nevil")
    # choice = int(input())
    # if choice == 1:
    print("Result = {}".format(Linear_Method(tab, xf)))
    # if choice == 2:
    print("Result = {}".format(Polynomial_Method(tab1, xf)))
    # if choice == 3:
    print("Result = {}".format(Lagrange_Method(tab2, xf)))
    # if choice == 4:
    print("Result = {}".format(Nevil_Method(tab3, xf)))


driver()


#
# # ______________________________________________________________________________________________________________
# # Cubic Spline Interpolation
# # ______________________________________________________________________________________________________________
# # In general form, Cubic Spline Interpolation takes N points: (x0,y0), (x1, y1), (x2, y2)
# # and calculate N-1 functions S0(x), S1(x).. with the following form:
# # si(x) = ai + bi(x-xi) + ci(x-xi)^2 + di(x-xi)^3, for x in rage [xi,yi]
# # in the program we will calculate the coefficients = [ a0,a1,a2..., b0,b1,b2..., c0, c1,c2... , d0,d1,d2...]
# #
# # ______________________________________________________________________________________________________________
#
#
# # simple class to store points (x,y)
# class Point:
#     def __init__(self, x, y):
#         self.x = float(x)
#         self.y = float(y)
#
#
# # receives array of points, and return cubic spline coefficients
# def Spline(points):
#     N = len(points) - 1
#     h = [(points[i + 1].x - points[i].x) for i in range(N)]  # delta x
#     b = [(points[i + 1].y - points[i].y) / h[i] for i in range(N)]  # delta y / delta x
#     ftt = [0] + [3 * (b[i + 1] - b[i]) / (h[i + 1] + h[i]) for i in range(N - 1)] + [
#         0]  # f''(x) = 0 for first and last element, for the rest: 3*(b(i+1)-bi)/(h(i+1)+hi)
#     A = [(ftt[i + 1] - ftt[i]) / (6 * h[i]) for i in range(N)]  # calc a0,a1,..
#     B = [ftt[i] / 2 for i in range(N)]  # calc b0,b1...
#     C = [b[i] - h[i] * (ftt[i + 1] + 2 * ftt[i]) / 6 for i in range(N)]  # calc c0,c1...
#     D = [points[i].y for i in range(N)]  # calc d0,d1...
#     return A, B, C, D
#
#
# # receives points and Spline coefficients and print the functions
# def PrintSpline(points, A, B, C, D):
#     for i in range(len(points) - 1):
#         func = '[' + str(points[i].x) + ',' + str(points[i + 1].x) + '] f(x) = '
#         components = []
#         if A[i]:
#             components.append(str(A[i]) + '(x-' + str(points[i].x) + ')^3')
#         if B[i]:
#             components.append(str(B[i]) + '(x-' + str(points[i].x) + ')^2')
#         if C[i]:
#             components.append(str(C[i]) + '(x-' + str(points[i].x) + ')')
#         if D[i]:
#             components.append(str(D[i]))
#         if components:
#             func += components[0]
#             for i in range(1, len(components)):
#                 if components[i][0] == '-':
#                     func += ' - ' + components[i][1:]
#                 else:
#                     func += ' + ' + components[i]
#             print(func)
#         else:
#             print(func + '0')
#
#
# def run_example(points):
#     print("points: ")
#     points = [Point(x, y) for x, y in points]
#     for point in points:
#         print("(" + str(point.x) + "," + str(point.y) + ")", end=" ")
#     print("")
#     print("Cubic spline interpolation:")
#     A, B, C, D = Spline(points)
#     PrintSpline(points, A, B, C, D)
#     print("")
#
#
# # Example A
# print("example A:")
# run_example([(1, 2), (2, 3), (3, 5)])
#
# # Example B
# print("example B:")
# run_example([(1, 0), (2, 1), (3, 0), (4, 1), (5, 0)])

