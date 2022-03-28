import math


def initMatrix(sizeA, sizeB):
    result = sizeA * [None]
    for i in range(sizeA):
        result[i] = sizeB * [0]
    return result


def createIdentityMatrix(n):
    Identity = []
    lst = []
    for i in range(n):
        for j in range(n):
            if i == j:
                lst.append(1)
            else:
                lst.append(0)
        Identity.append(lst)
        lst = []
    return Identity


def elementarMatrix(n, index1, index2, number):
    IdentityMatrix = createIdentityMatrix(n)
    IdentityMatrix[index1][index2] = number
    return IdentityMatrix


def changeResult(B, index1, index2):
    temp = B[index1]
    temp1 = B[index2]
    B[index1] = temp1
    B[index2] = temp
    return B


def elementaryMatrixUnique(n, index1, index2, number):
    elementary = createIdentityMatrix(len(n))
    if index1 == 0 and index2 == 2 or index1 == 2 and index2 == 0:
        temp = elementary[index1]
        temp1 = elementary[index2]
        elementary[index1] = temp1
        elementary[index2] = temp
        return elementary
    if index1 == 0 and index2 == 1 or index1 == 1 and index2 == 0:
        temp = elementary[index1]
        temp1 = elementary[index2]
        elementary[index1] = temp1
        elementary[index2] = temp
        return elementary
    if index1 == 1 and index2 == 2 or index1 == 2 and index2 == 1:
        temp = elementary[index1]
        temp1 = elementary[index2]
        elementary[index1] = temp1
        elementary[index2] = temp
        return elementary


def funcPrint(A):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                                  for row in A]))


def Multiple(k, A):
    sizeA = len(A)
    sizeB = len(A[0])
    result = initMatrix(sizeA, sizeB)
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] * k
    return result






def Multiplication(M1, M2):
    size1 = len(M1)
    size2 = (len(M1[0]))
    size3 = len(M2)
    size4 = len(M2[0])
    if size2 != size3:
        return ArithmeticError("the size is not correct")
    result = initMatrix(size1, size4)
    for i in range(size1):
        for j in range(size4):
            for k in range(size2):
                result[i][j] += M1[i][k] * M2[k][j]


    return result


def InverseMatrice(A, B):
    trueelementary = A
    lst = []
    lst2 = []
    lst3 = []
    bMatrix = B
    counter = 1
    determinant = getMatrixDeternminant(trueelementary)
    if determinant == 0:
        raise "There's is no inverse"
    else:
        counter1 = 0
        counter2 = -1
        for i in range(len(trueelementary)):
            temp = trueelementary[i][i]
            counter2 = i
            counter1 = 0
            for j in range(len(trueelementary[i])):
                if j >= i:
                    if abs(trueelementary[j][i]) > abs(temp):
                        counter1 += 1 + i
                        temp = trueelementary[j][i]
            if counter1 == 0:
                pass
            else:
                if i == 0:
                    if counter1 == 1:
                        elementary = elementaryMatrixUnique(trueelementary, counter1 + 1, counter2, 1)
                        #bMatrix = changeResult(B, counter1 + 1, counter2)
                        lst2.append(elementary)
                        print("Elementary : {}".format(counter))
                        funcprintt(elementary)
                        print("\n")
                        print("Matrix A :")
                        funcprintt(trueelementary)
                        print("\n")
                        trueelementary = Multiplication(elementary, trueelementary)
                        print("Elementary {} multiply by the Matrix X : ".format(counter))
                        funcprintt(trueelementary)
                        print("\n")
                        print(
                            "==========================================================================================")
                        print("\n")
                    else:
                        elementary = elementaryMatrixUnique(trueelementary, counter1, counter2, 1)
                        #bMatrix = changeResult(B, counter1, counter2)
                        lst2.append(elementary)
                        print("Elementary : {}".format(counter))

                        funcprintt(elementary)
                        print("\n")
                        print("Matrix A :")
                        funcprintt(trueelementary)
                        print("\n")
                        trueelementary = Multiplication(elementary, trueelementary)
                        print("Elementary {} multiply by the Matrix X : ".format(counter))
                        counter += 1
                        funcprintt(trueelementary)
                        print("\n")
                        print(
                            "==========================================================================================")
                        print("\n")
                else:
                    elementary = elementaryMatrixUnique(trueelementary, counter1, counter2, 1)
                    #bMatrix = changeResult(B, counter1, counter2)
                    lst2.append(elementary)
                    print("Elementary : {}".format(counter))
                    funcprintt(elementary)
                    print("\n")
                    print("Matrix A :")
                    funcprintt(trueelementary)
                    print("\n")
                    trueelementary = Multiplication(elementary, trueelementary)
                    print("Elementary {} multiply by the Matrix X : ".format(counter))
                    counter += 1
                    funcprintt(trueelementary)
                    print("\n")
                    print("==========================================================================================")
                    print("\n")



        for i in range(len(trueelementary)):
            if trueelementary[i][i] != float(1) and i < len(trueelementary) or trueelementary[i][i] != int(
                    1) and i < len(trueelementary):
                b = 1 / trueelementary[i][i]
                elementary = elementarMatrix(len(trueelementary), i, i, b)
                print("Elementary : {}".format(counter))
                funcprintt(elementary)
                print("\n")
                print("Matrix A :")
                funcprintt(trueelementary)
                print("\n")
                trueelementary = Multiplication(elementary, trueelementary)
                print("Elementary {} multiply by the Matrix X : ".format(counter))
                counter += 1
                funcprintt(trueelementary)
                print("\n")
                print("==========================================================================================")
                print("\n")
                lst.append(trueelementary)
                lst2.append(elementary)
            for j in range(len(trueelementary[i])):
                if j != i and trueelementary[j][i] != int(0) and j > i or j != i and trueelementary[j][i] != float(
                        0) and j > i:
                    d = (trueelementary[j][i] / trueelementary[i][i]) * -1
                    elementary = elementarMatrix(len(trueelementary), j, i, d)
                    print("Elementary : {}".format(counter))
                    funcprintt(elementary)
                    print("\n")
                    print("Matrix A :")
                    funcprintt(trueelementary)
                    print("\n")
                    trueelementary = Multiplication(elementary, trueelementary)
                    print("Elementary {} multiply by the Matrix X : ".format(counter))
                    counter += 1
                    funcprintt(trueelementary)
                    print("\n")
                    print("==========================================================================================")
                    print("\n")
                    lst.append(trueelementary)
                    lst2.append(elementary)
                    # lst3.append(bMatrix)
        for i in range(len(trueelementary) - 1, -1, -1):
            for j in range(len(trueelementary[i]) - 1, -1, -1):
                if trueelementary[i][j] != int(0) and trueelementary[i][j] != float(0.0) and trueelementary[i][
                    j] != int(1) and trueelementary[i][j] != float(1.0) and trueelementary[i][j] and i != j:
                    d = (trueelementary[i][j] / trueelementary[i][i]) * -1
                    elementary = elementarMatrix(len(trueelementary), i, j, d)
                    print("Elementary : {}".format(counter))
                    funcprintt(elementary)
                    print("\n")
                    print("Matrix A :")
                    funcprintt(trueelementary)
                    print("\n")
                    trueelementary = Multiplication(elementary, trueelementary)
                    print("Elementary {} multiply by the Matrix X : ".format(counter))
                    counter += 1
                    funcprintt(trueelementary)
                    print("\n")
                    print("==========================================================================================")
                    print("\n")
                    lst.append(trueelementary)
                    lst2.append(elementary)
        temp = lst2[0]
        for i in range(1, len(lst2), 1):
            temp2 = lst2[i]
            temp = Multiplication(temp2, temp)
        print("Inverse Matrix :")
        funcprintt(temp)
        print("\n")
        print("==========================================================================================")
        print("\n")
        print("Vector X : ")
        print(Multiplication(temp, bMatrix))


def funcprintt(A):
    print('\n'.join(['             '.join(['{:4}'.format(item) for item in row])
                     for row in A]))


# for i, j in zip(A, B):
# print(j, " * ", i, " = ")

def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrixDeternminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant


A = [[0.04, 0.01, -0.01], [0.2, 0.5, -0.2], [1, 2, 4]]
B = [[0.06], [0.3], [11]]

InverseMatrice(A, B)
