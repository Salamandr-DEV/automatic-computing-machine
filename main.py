''''#скалярное умножение векторов

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2]

B = [5, 6, 8, 4, 6, 4, 3, 2, 1, 0, 3]

def Scalar(a, b):
    D = []
    if len(a) != len(b):
        #print("Разная длина векторов")
        return "Разная длина векторов"
    else:
        for i in range(len(a)):
            D.append(A[i] * B[i])
    return D
print(Scalar(A, B))'''

#умножение матриц

A = []
B = []
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(2)
    A.append(temp)
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(2)
    B.append(temp)

print(A)
print(B)

def Matrix(a, b):
    D = []
    counter = 0
    for i in range(len(a[0])):
        temp = []
        for j in range(len(b)):
            temp.append(0)
        D.append(temp)
    print(D)
    if len(a) != len(b[0]):
        return "Разная длина матриц"
    else:
        for i in range(len(D)):
            for j in range(len(D[0])):
                for k in range(len(D)):
                    D[i][j] = a[i][k] * b[k][j]
                    counter = counter + D[i][j]
                D[i][j] = counter
                counter = 0
    return D
print(Matrix(A, B))





