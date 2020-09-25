import numpy
import math


def linearRegression(X, Y):
    A = numpy.array([[i, 1] for i in X])
    B = numpy.array([[i] for i in Y])
    LR = numpy.dot(numpy.linalg.inv(
        numpy.dot(numpy.transpose(A), A)), numpy.dot(numpy.transpose(A), B))
    #y = ax + b
    EQ = LR[0]*X+LR[1]
    DE = "y = " + str(round(float(LR[0]), 5)) + \
        "x + " + str(round(float(LR[1]), 5))
    ANS = [EQ, DE]
    return ANS


def polynominomialRegression(X, Y, G):
    A = numpy.array([[pow(j, i) for i in range(G, -1, -1)] for j in X])
    B = numpy.array([[i] for i in Y])
    PR = numpy.dot(numpy.linalg.inv(
        numpy.dot(numpy.transpose(A), A)), numpy.dot(numpy.transpose(A), B))
    #y = a1*x^n + a2*x^n-1 + ... + an*x^0
    X = numpy.arange(1, 25, 0.1)
    EQ = 0
    DE = "y = "
    j = 0
    for i in range(G, -1, -1):
        EQ += PR[j] * pow(numpy.array(X), i)
        if i > 1:
            DE += str(round(float(PR[j]), 5)) + "x^" + str(i) + " + "
        elif i == 1:
            DE += str(round(float(PR[j]), 5)) + "x  + "
        else:
            DE += str(round(float(PR[j]), 5))
        j += 1
    ANS = [EQ, DE]
    return ANS


def potentialRegression(X, Y):
    A = numpy.array([[1, math.log(i)] for i in X])
    B = numpy.array([[math.log(i)] for i in Y])
    PoR = numpy.dot(numpy.linalg.inv(
        numpy.dot(numpy.transpose(A), A)), numpy.dot(numpy.transpose(A), B))
    PoR[0] = pow(math.e, PoR[0])
    #y = ax^b
    X = numpy.arange(1, 25, 0.1)
    EQ = PoR[0]*pow(X, PoR[1])
    DE = "y = " + str(round(float(PoR[0]), 5)) + \
        "x^" + str(round(float(PoR[1]), 5))
    ANS = [EQ, DE]
    return ANS


def exponentialRegression(X, Y):
    A = numpy.array([[1, i] for i in X])
    B = numpy.array([[math.log(i)] for i in Y])
    ER = numpy.dot(numpy.linalg.inv(
        numpy.dot(numpy.transpose(A), A)), numpy.dot(numpy.transpose(A), B))
    ER[0] = pow(math.e, ER[0])
    #y = ae^(bx)
    X = numpy.arange(1, 25, 0.1)
    EQ = ER[0]*pow(math.e, ER[1]*X)
    DE = "y = " + str(round(float(ER[0]), 5)) + \
        "e^(" + str(round(float(ER[1]), 5)) + "x)"
    ANS = [EQ, DE]
    return ANS
