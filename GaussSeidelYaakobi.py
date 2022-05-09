from functools import reduce


def printVector(vec):
    """
    A function that prints a vector

    :param vec: Vector to print
    :return: No return value
    """
    for i in range(len(vec)):
        vec[i] = round(vec[i], 4)
        print(vec[i])


def printMatrix(matrix):
    """
    A function that prints a matrix

    :param matrix: A matrix to print
    :return:  No return value
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{: ^20}'.format(matrix[i][j]), end="")
        print('\n')


def copy_matrix(A):
    """
    A function that

    :param A: A matrix to copy
    :return: The new copied matrix
    """
    matrixC = [[A[y][x] for x in range(len(A))] for y in range(len(A))]
    return matrixC


def determinant_recursive(A, total=0):
    """
    A recursive function that calculates the determinant of a given matrix

    :param A: A matrix
    :param total: A parameter used in the function that hold the current total, it's default is zero
    :return: The determinant of matrix A
    """
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]
        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det
    return total


def I_matrix(A):
    """
    A function that generates a I matrix

    :param A: A matrix, used to make the I matrix the same size the parameter matrix
    :return: I matrix in the same size as the given matrix (parameter)
    """
    matrixC = [[0 for x in range(len(A))] for y in range(len(A))]
    for i in range(len(A)):
        matrixC[i][i] = 1
    return matrixC


def matrix_vectorMul(matrixA, vecA):
    """
    A function that multiplies a matrix and a vector and checks if they are: 1. Square matrix
                                                                             2. In the same size
    ** If one of the two above is False the program will stop **
    Then the function will multiply them according to the according to the multiplication algorithm

    :param matrixA: The matrix is in the left side of the multiplication
    :param vecA: The vector is in the right side of the multiplication
    :return: A new vector, it represents the results
    """
    if len(matrixA) == len(vecA) and len(matrixA) == len(matrixA[0]):  # checks the size of the matrix and the vector
        for i in range(len(matrixA)):  # checks if the left matrix is square
            if len(matrixA) != len(matrixA[i]):
                raise "Cant Multiply"
    newVec = [0 for i in range(len(vecA))]  # Generating a new vector for the result
    for i in range(len(matrixA)):  # multiplication according to the multiplication algorithm
        for j in range(len(vecA)):
            newVec[i] += matrixA[i][j] * vecA[j]
    return newVec


def matrixMul(matrixA, matrixB):
    """
    A Function that gets 2 matrices and checks if they are: 1. Square matrix
                                                            2. In the same size
    ** If one of the two above is False the program will stop **
    Then the function will multiply them according to the according to the multiplication algorithm

    :param matrixA: The matrix at the left of the multiplication
    :param matrixB:The matrix at the right of the multiplication
    :return: A new matrix, it represents the results
    """
    if len(matrixA) == len(matrixB) and len(matrixA) == len(matrixA[0]):  # checks the sizes of the both matrices
        for i in range(len(matrixA)):  # checks if the left matrix is square
            if len(matrixA) != len(matrixA[i]):
                raise "Not NxN"
        for i in range(len(matrixB)):  # checks if the left matrix is square
            if len(matrixB) != len(matrixB[i]):
                raise "Not NxN"
        matrixC = [[0 for x in range(len(matrixA))] for y in
                   range(len(matrixB))]  # Generating a new matrix for the result
        for i in range(len(matrixC)):  # multiplication according to the multiplication algorithm
            for j in range(len(matrixC)):
                for k in range(len(matrixC)):
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        return matrixC
    else:
        raise "Not NxN / same size"


def pivotMatrix(matrix):
    """
    arrange the matrix so the pivot will be in the diagonal
    :param matrix:the matrix to arrange
    :return:the arrange matrix
    """
    matrixes = []  # A List for all of the mid matrices along the solution
    for i in range(len(matrix)):
        flag = i
        Mmax = matrix[i][i]
        for j in range(i, len(matrix)):
            if matrix[i][j] > Mmax:
                flag = j
                Mmax = matrix[i][j]
        if flag != i:
            temp = matrix[i]
            matrix[i] = matrix[flag]
            matrix[flag] = temp
            matrixes.append(matrix)
    return matrix, matrixes


def ifDominant(matrix):
    """
    check if dominant matrix
    :param matrix: the matrix to check
    :return: true if dominant false if not
    """
    for i in range(0, len(matrix)):
        sum = 0
        for j in range(0, len(matrix)):
            sum = sum + abs(matrix[i][j])
        sum = sum - abs(matrix[i][i])
        if (abs(matrix[i][i]) < sum):
            return False
    return True


def LDU(matrix):
    """
    calc the L D and U parameters of the matrix

    :param matrix: matrix to calc its parameters
    :return: L D and U
    """
    L, D, U = I_matrix(matrix), I_matrix(matrix), I_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > j:
                L[i][j] = matrix[i][j]
            if i == j:
                L[i][i] = 0
                U[i][i] = 0
                D[i][i] = matrix[i][i]
            if i < j:
                U[i][j] = matrix[i][j]
    return L, D, U


def addMatrices(A, B):
    """
    calc the sum of 2 matrices

    :param A: 1 matrix
    :param B: 2 matrix
    :return: the sum of the 2 matrices
    """
    if len(A) == len(B) and len(A) == len(A[0]) and len(B) == len(B[0]):
        C = I_matrix(A)
        for i in range(len(A)):
            for j in range(len(A)):
                C[i][j] = A[i][j] + B[i][j]
        return C
    raise ("Not n*n or not the same size")


def GHjaacobi(matrix):
    """
    calc G and H parameters by jaacobi

    :param matrix: the given matrix
    :return: the calc of G and H
    """
    L, D, U = LDU(matrix)
    H = getMatrixInverse(D)
    G = copy_matrix(H)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            G[i][j] = -1 * G[i][j]
    G = matrixMul(G, addMatrices(L, U))
    return G, H


def GHGaussSeidel(matrix):
    """
        calc G and H parameters by GaussSeidel

        :param matrix: the given matrix
        :return: the calc of G and H
        """
    L, D, U = LDU(matrix)
    H = getMatrixInverse(addMatrices(L, D))
    G = copy_matrix(H)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            G[i][j] = -1 * G[i][j]
    G = matrixMul(G, U)
    return G, H


def addVec(A, B):
    """
       calc the sum of 2 vectors

       :param A: 1 vector
       :param B: 2 vector
       :return: the sum of the 2 vectors
       """
    c = []
    if len(A) == len(B):
        for i in range(len(A)):
            c.append(A[i] + B[i])
        return c
    else:
        raise "Vectors not the same size"


def machineEpsilon(func=float):  # This is a function from assignment 1
    """
    A recursive function that calculates the machine epsilon

    :param func: A parameter that is a function, default if float
    :return: The machine epsilon
    """
    machine_epsilon = func(1)
    machine_epsilon_last = 0.0
    while func(1) + machine_epsilon != func(1):
        machine_epsilon_last = machine_epsilon
        machine_epsilon = func(machine_epsilon) / func(2)
    return machine_epsilon_last


def transposeMatrix(m):
    """
    calc the transpose matrix

    :param m:the given matrix
    :return: her transpose
    """
    return list(map(list, zip(*m)))


def getMatrixMinor(m, i, j):
    """
       calc the minor of the matrix

       :param m:the given matrix
       :return: her minor
       """
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrixInverse(m):
    """
    calc the inverse matrix of the matrix

    :param m:the given matrix
    :return:the inverse matrix
    """
    determinant = determinant_recursive(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * determinant_recursive(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            if (abs(cofactors[r][c] / determinant) <= machineEpsilon()):
                cofactors[r][c] = 0
            else:
                cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def Jaacobi(matrix, vec):
    """
    calc by jaacobi method

    :param matrix: given matrix
    :param vec: vector
    :return: the calc of the linear equation
    """
    matrixes = []
    matrix, temp = pivotMatrix(matrix)
    matrixes += temp
    isdom = False
    if (ifDominant(matrix)):
        isdom = True
    else:
        print("Pay attention, there is no dominant diagonal")
    G, H = GHjaacobi(matrix)
    vec0 = []
    for i in range(len(vec)):
        vec0.append(0)
    if isdom:
        x = -1
    else:
        x = 100
    counter = 1
    print("0." + str(vec0))
    while (x != 0):
        tempVec = vec0
        vec0 = addVec(matrix_vectorMul(G, vec0), matrix_vectorMul(H, vec))
        print(str(counter) + "." + str(vec0))
        print()
        flag = 0
        for i in range(len(vec0)):
            if abs(tempVec[i] - vec0[i]) >= 0.00001:
                flag = 1
        if flag == 0: break
        x -= 1
        counter += 1
    return vec0,counter


def GausseSeidel(matrix, vec):
    """
    calc by Gausse Seidel method

    :param matrix: given matrix
    :param vec: vector
    :return: the calc of the linear equation
    """
    matrixes = []
    matrix, temp = pivotMatrix(matrix)
    matrixes += temp
    isdom = False
    if (ifDominant(matrix)):
        isdom = True
    else:
        print("Pay attention, there is no dominant diagonal")
    G, H = GHGaussSeidel(matrix)
    vec0 = []
    for i in range(len(vec)):
        vec0.append(0)
    if isdom:
        x = -1
    else:
        x = 100
    counter = 1
    print("0." + str(vec0))
    while (x != 0):
        tempVec = vec0
        vec0 = addVec(matrix_vectorMul(G, vec0), matrix_vectorMul(H, vec))
        print(str(counter) + "." + str(vec0))
        print()
        flag = 0
        for i in range(len(vec0)):
            if abs(tempVec[i] - vec0[i]) >= 0.00001:
                flag = 1
        if flag == 0: break
        x -= 1
        counter += 1
    return vec0,counter


matrixA = [[25, 5, 1],
     [4, 2, 1],
     [1, 1, 1]]
vectorB = [2, 0, 1]

while(True):
    choice = input("Press 1 for Jaacobi or 2 for Gausse-Seidel (anything else to exit): ")
    if choice == "1":
        x, y = Jaacobi(matrixA, vectorB)
        print("Number of iterations: " + str(y))
        printVector(x)
        print()
    elif choice == "2":
        x,y = GausseSeidel(matrixA, vectorB)
        print("Number of iterations: " + str(y))
        printVector(x)
        print()
    else:
        break

