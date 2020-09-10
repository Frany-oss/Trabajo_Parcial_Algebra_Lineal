
import random


def generar_arreglo():
    a = []
    for i in range(50):
        rand = random.randint(0, 25)
        a.append(rand)
    return a

def generar_pares(arreglo, n):
    used_pairs = set()
    used_axis_X = []
    count = 0
    while True:
        pair = random.sample(arreglo, 2)
        pair = tuple(sorted(pair))
        if pair not in used_pairs and pair[0] not in used_axis_X:
            used_axis_X.append(pair[0])
            used_pairs.add(pair)
            count += 1
            if count == n:
                break
    # print(used_axis_X)
    return used_pairs
