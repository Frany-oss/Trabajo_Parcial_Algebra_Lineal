import numpy as np
import math

def regresion_lineal(X, Y, n = 0):
    X_o = X

    unos = np.array([np.ones(n)])
    X = np.append(X, unos, axis=0)
    X = np.rot90(X, 3)
    Y = np.rot90(Y, 3)
    R = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

    YR = X_o*R[1][0]+R[0][0]

    return YR


def regresion_polinomial(X, Y, n, a):

    X_o = X
    unos = np.array([np.ones(n)])
    X_e = X**a
    X = np.append(unos, X, axis=0)
    X = np.append(X, X_e, axis=0)
    X = np.rot90(X, 3)
    Y = np.rot90(Y, 3)
    R = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

    # YR = X_2*R[0][0]+R[1][0]*X_o + R[2][0]
    x = np.array([np.arange(25)])
    x_a = x**a
    YR = x_a*R[0][0]+R[1][0]*x + R[2][0]
    return x, YR


def regresion_potential(x, y, n):
    A = np.array([np.ones(n)])
    B = np.array([[np.log10(i)] for i in y])

    lna, b = regresion_lineal(A, B, n)
    a = pow(math.e, lna)
   
    x1 = [i for i in range(2, 14)]
    y1 = [a*pow(i, b) for i in x]

    return x, y1


def regresion_exponencial(x, y, n):
    A = np.array([np.ones(n)])
    B = np.array([[np.log10(i)] for i in y])

    lna, b = regresion_lineal(A, B, n)
    a = pow(math.e, lna)
    x1 = [i for i in range(2,14)]
    y1 = [a*pow(math.e, b*i) for i in x]

    return x, y1
