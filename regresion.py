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
    pass
