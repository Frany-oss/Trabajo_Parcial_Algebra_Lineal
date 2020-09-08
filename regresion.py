import numpy as np


def regresion_lineal(X, Y, n):
    X_o = X

    unos = np.array([np.ones(n)])
    X = np.append(X, unos, axis=0)
    X = np.rot90(X, 3)
    Y = np.rot90(Y, 3)
    R = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

    YR = X_o*R[1][0]+R[0][0]

    return YR


def regresion_polinomial(X, Y, n):

    X_o = X
    unos = np.array([np.ones(n)])
    X_2 = X**2
    X = np.append(unos, X, axis=0)
    X = np.append(X, X_2, axis=0)
    X = np.rot90(X, 3)
    Y = np.rot90(Y, 3)
    R = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

    # YR = X_2*R[0][0]+R[1][0]*X_o + R[2][0]
    x = np.array([np.arange(25)])
    x_2 = x**2
    YR = x_2*R[0][0]+R[1][0]*x + R[2][0]
    return x, YR


def regresion_exponencial(X, Y, n):
    X_o = X
    unos = np.array([np.ones(n)])
    pass
