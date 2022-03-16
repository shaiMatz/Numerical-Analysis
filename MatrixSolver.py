def matrixMul(matrixA, matrixB):
    if lenI(matrixA)==len(matrixA[0]) and len(matrixB)==len(matrixB[0]) and len(matrixA)==len(matrixB):
        matrixC = [[0 for x in range(len(matrixA))] for y in range(len(matrixB))]
        for i in range(len(matrixC)):
            for j in range(len(matrixC)):
                for k in range(len(matrixC)):
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        return matrixC
    else:
        print("Not NxN / same size")

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



def matrixSolve(matrix):
    if lenI(matrix) == len(matrix) and determinant_recursive(matrix)!=0:
        solve=[[0 for x in range(len(matrix))] for y in range(len(matrix))]

