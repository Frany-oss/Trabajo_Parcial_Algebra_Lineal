import numpy as np
import math


def regresion(A, B):
    # Rotar matrices
    A = np.rot90(A, 3)
    B = np.rot90(B, 3)
    # Calcular con la fórmula
    multi_1 = np.dot(A.T, A)
    multi_2 = np.dot(A.T, B)
    R = np.dot(np.linalg.inv(multi_1), multi_2)

    return R


def regresion_lineal(X, Y):

    n = len(X[0])
    # creas la matriz y le agregas una columna de 1s
    unos = np.array([np.ones(n)])
    A = np.append(X, unos, axis=0)
    R = regresion(A, Y)

    YR = X*R[1][0]+R[0][0]

    return YR


def regresion_polinomial(X, Y, grado):
    n = len(X[0])
    # maximo elemento de X
    max_n = X[0][n-1]

    for g in range(0, grado+1):
        if g == 0:
            A = np.array([np.ones(n)])
        else:
            X_e = X**g
            A = np.append(A, X_e, axis=0)

    R = regresion(A, Y)

    X_i = np.array([np.arange(1, max_n+1, 0.1)])
    YR = np.array([np.zeros((max_n+1)*10)])
    for i in range(grado+1):
        g = grado - i
        X_a = X_i**g
        YR = YR + X_a*R[i][0]

    return X_i, YR


def regresion_potential(x, y, n):
    A = np.array([np.ones(n)])
    B = np.array([[np.log10(i)] for i in y])

    lna, b = regresion_lineal(A, B, n)
    a = pow(math.e, lna)

    x1 = [i for i in range(2, 14)]
    y1 = [a*pow(i, b) for i in x]

    return x, y1


def regresion_exponencial(X, Y):
    n = len(X[0])
    max_n = X[0][n-1]
    unos = np.array([np.ones(n)])
    logX = np.log(X)
    A = np.append(logX, unos, axis=0)
    B = np.log(Y)
    R = regresion(A, B)
    X_i = np.array([np.arange(1, max_n+1, 0.1)])
    YR = pow(math.e, R[0][0])*pow(X_i, R[1][0])
    print(YR)
    return X_i, YR
