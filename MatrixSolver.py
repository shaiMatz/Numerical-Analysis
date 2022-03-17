def matrixMul(matrixA, matrixB):
    if len(matrixA) == len(matrixB) and len(matrixA) == len(matrixA[0]):
        for i in range(len(matrixA)):
            if len(matrixA) != len(matrixA[i]):
                exit(0)
        for i in range(len(matrixB)):
            if len(matrixB) != len(matrixB[i]):
                exit(0)
        matrixC = [[0 for x in range(len(matrixA))] for y in range(len(matrixB))]
        for i in range(len(matrixC)):
            for j in range(len(matrixC)):
                for k in range(len(matrixC)):
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        return matrixC
    else:
        print("Not NxN / same size")


def matrix_vectorMul(matrixA, vecA):
    if len(matrixA) == len(vecA) and len(matrixA) == len(matrixA[0]):
        for i in range(len(matrixA)):
            if len(matrixA) != len(matrixA[i]):
                raise "Cant Multiply"
    newVec = [0 for i in range(len(vecA))]
    for i in range(len(matrixA)):
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
        print('\t'.join(map(str, i)))

def Norm_Of_A_Matrix(matrix):
    temp = [0 for x in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp[i] += abs(matrix[i][j])
    return max(temp)

X = [[0, 0, 0,1],
     [0, -5, 1,0],
    [0, -3, 0,0],
     [1,0,1,0]
]
#print(matrixSolve(X, [1, 2, 3,4]))
print(Norm_Of_A_Matrix(X))
