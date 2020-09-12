import numpy as np
import matplotlib.pyplot as plt
import math


def lineal_regression(A, B):
    x = np.dot(np.transpose(A), A)
    y = np.dot(np.transpose(A), B)
    return np.dot(np.linalg.inv(x), y)


x = [i for i in range(4, 8)]
y = [20, 22.4, 24.5, 26.5]

# POLYNOMIAL y = a*x^2 + b*x + c


def polynomial(x, y, n):

    A = np.array([[pow(j, i) for i in range(n, -1, -1)]for j in x])
    B = np.array([[i] for i in y])
    result = lineal_regression(A, B)
    print(result)
    x1 = [i for i in range(2, 14)]
    y1 = []
    for base in x:
        j = 0
        sum = 0
        for i in range(n, -1, -1):
            sum += result[j]*pow(base, i)
            j += 1
        y1.append(sum)

    # y1 = [a*pow(i,2) + b*i + c for i in x]
    return x, y1

# Potential y = a*x^b


def potential(x, y):
    A = np.array([[1, math.log(i)] for i in x])
    B = np.array([[math.log(i)] for i in y])
    lna, b = lineal_regression(A, B)
    a = pow(math.e, lna)
    print(a, b)
    x1 = [i for i in range(2, 14)]
    y1 = [a*pow(i, b) for i in x]
    return x, y1

# EXPONENTIAL y = ax^b


def exponential(x, y):
    A = np.array([[1, i] for i in x])
    B = np.array([[math.log(i)] for i in y])
    lna, b = lineal_regression(A, B)
    a = pow(math.e, lna)
    print(a, b)
    x1 = [i for i in range(2, 14)]
    y1 = [a*pow(math.e, b*i) for i in x]
    return x, y1


def showGraph(x, y, regression_type):
    if regression_type == polynomial:
        n = int(input("Ingrese n: "))
        x, y1 = regression_type(x, y, n)
    else:
        x, y1 = regression_type(x, y)

    print(y1)
    plt.plot(x, y1)
    plt.plot(x, y, 'ro')
    plt.show()


# showGraph(x, y, polynomial)
showGraph(x, y, potential)
# showGraph(x, y, exponential)
