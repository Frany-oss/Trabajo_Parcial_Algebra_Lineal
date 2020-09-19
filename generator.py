
import random

def generateArray(n,order):	
	X = list(range(1, 26))
	for i in range(25-n):
		del X[random.randint(0, len(X)-1)]
	Y = [0]*n
	for i in range(n):
		Y[i] = random.randint(1, 26)
	if order:
		Y.sort()
	return X,Y