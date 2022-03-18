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
                exit(0)
            else:
                print("Not NxN")
        for i in range(len(matrixB)):  # checks if the left matrix is square
            if len(matrixB) != len(matrixB[i]):
                exit(0)
            else:
                print("Not NxN")
        matrixC =[[0 for x in range(len(matrixA))] for y in range(len(matrixB))]  # Generating a new matrix for the result
        for i in range(len(matrixC)):  # multiplication according to the multiplication algorithm
            for j in range(len(matrixC)):
                for k in range(len(matrixC)):
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        return matrixC
    else:
        print("Not NxN / same size")


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
    for i in range(len(matrixA)): # multiplication according to the multiplication algorithm
        for j in range(len(vecA)):
            newVec[i] += matrixA[i][j] * vecA[j]
    return newVec


def machineEpsilon(func=float):
    machine_epsilon = func(1)
    machine_epsilon_last = 0.0
    while func(1) + machine_epsilon != func(1):
        machine_epsilon_last = machine_epsilon
        machine_epsilon = func(machine_epsilon) / func(2)
    return machine_epsilon_last


def I_matrix(A):
    matrixC = [[0 for x in range(len(A))] for y in range(len(A))]
    for i in range(len(A)):
        matrixC[i][i] = 1
    return matrixC


"""
X = [[12, 7, -4],
     [4, 5, 6],
     [7, 8, 9]]
# 3x4 matrix
Y = [[5, 8, 1],
     [6, 7, 3],
     [-9, 5, 9]]
# result is 3x4
result = [[ 0, 0, 0],
          [ 0, 0, 0],
          [ 0, 0, 0]]
result=matrixMul(X,Y)
for i in range(3):
    print(result[i])"""


def copy_matrix(A):
    matrixC = [[A[y][x] for x in range(len(A))] for y in range(len(A))]
    return matrixC


def determinant_recursive(A, total=0):
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


def matrixSolve(matrix, vecB):
    elementary = []
    matrixes=[]
    matrixes.append(matrix)
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]) or len(matrix)!=len(vecB):
            raise "not NxN or vector is not the same size of matrix"
    if determinant_recursive(matrix) != 0:
        solve = I_matrix(matrix)
        for i in range(len(matrix)):
            if matrix[i][i] == 0.0 or abs(matrix[i][i]) - machineEpsilon() < 0.0:
                k = i
                while k < len(matrix) and matrix[k][i] == 0:
                    k += 1
                temp = solve[i]
                solve[i] = solve[k]
                solve[k] = temp
                elementary.append(solve)
                matrix = matrixMul(solve, matrix)
                matrixes.append(matrix)
            if matrix[i][i] != 1:
                solve = I_matrix(matrix)
                solve[i][i] = 1 / matrix[i][i]
                elementary.append(solve)
                matrix = matrixMul(solve, matrix)
                matrixes.append(matrix)
            m = i + 1
            while m < len(matrix):
                if matrix[m][i] != 0 or abs(matrix[m][i]) - machineEpsilon() < 0:
                    solve = I_matrix(matrix)
                    solve[m][i] = -matrix[m][i] / matrix[i][i]
                    elementary.append(solve)
                    matrix = matrixMul(solve, matrix)
                    matrixes.append(matrix)
                m = m + 1
        n = len(matrix) - 1
        while n >= 0:
            m = n - 1
            while m >= 0:
                if matrix[m][n] != 0 or abs(matrix[m][n]) - machineEpsilon() < 0:
                    solve = I_matrix(matrix)
                    solve[m][n] = -matrix[m][n] / matrix[n][n]
                    elementary.append(solve)
                    matrix = matrixMul(solve, matrix)
                    matrixes.append(matrix)
                m = m - 1
            n = n - 1
        for i in elementary:
            vecB = matrix_vectorMul(i, vecB)

        return vecB
    else:
        raise "Error"

def printMatrix(matrix):
    for i in matrix:
        print('{: ^20} {: ^20} {: ^20} {: ^20}\n'.format(*i))

def Norm_Of_A_Matrix(matrix):
    temp = [0 for x in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp[i] += abs(matrix[i][j])
    return max(temp)

X = [[0, 0, 0,1],
     [0, 5.65165165166516516651651651651, 1,0],
    [0, -3, 0,0],
     [1,0,1,0]
]
#print(matrixSolve(X, [1, 2, 3,4]))
printMatrix(X)
