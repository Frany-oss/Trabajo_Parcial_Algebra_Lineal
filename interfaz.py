'''
Pida el ingreso de n[8,12] y genere aleatoriamente npares ordenados. 
El programa debemostrar gráficamente la curva que se aproxime mejor linealmente a los npares ordenados. 
El usuario debe seleccionar el tipo de curva: polinomial(de grado 𝑚≤6), exponencial o potencial.
'''
from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
import random
import numpy as np

# Inicializamos los globales
X = None
Y = None
N = None


def generar_arreglo():
    a = []
    for i in range(50):
        rand = random.randint(0, 25)
        a.append(rand)
    return a


def generar_pares(arreglo, n):
    used_pairs = set()
    used_axis_X = []
    n = numeroPares.get()
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


def generar_pares2(n):
    x_rand = random.sample(range(0, 100), n)
    y_rand = random.sample(range(0, 100), n)
    x_rand.sort()
    return x_rand, y_rand


def show_plot():
    global X, Y
    global N

    n = numeroPares.get()

    # Checkea si X y Y existen o si se pide otra cantidad de pares en el slider
    if n != N:
        N = n
        p = generar_pares(generar_arreglo(), N)
        X = []
        Y = []
        # print(p)
        for i in p:
            X.append(i[0])
            Y.append(i[1])
        print(X)
        # X, Y = generar_pares2(n)
        X.sort()
        X = np.array([X])
        Y = np.array([Y])
        print(X)

    YR = regresion_lineal(X, Y, n)

    #regression = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
    print(X, YR)
    plt.plot(X[0], Y[0], 'ro', X[0], YR[0])
    plt.title('Regresion Lineal')
    plt.show()


def regresion_lineal(X, Y, n):
    X_o = X

    unos = np.array([np.ones(n)])
    X = np.append(X, unos, axis=0)
    X = np.rot90(X, 3)
    Y = np.rot90(Y, 3)
    R = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

    YR = X_o*R[1][0]+R[0][0]

    return YR
# def regresion_lineal(x, y):
#     slope, intercept, r, p, std_err = stats.linregress(x, y)
#     myfunc = slope * x + intercept
#     mymodel = list(map(myfunc, x))

#     plt.scatter(x, y)
#     plt.plot(x, mymodel)
#     plt.show()


# --------- INTERFAZ DEL PROGRAMA -----------
root = Tk()
root.title('Regresión Lineal')
root.maxsize(600, 100)
root.geometry('600x100')
root.config(bg='white')


def exit():
    return root.destroy()


UI_frame = Frame(root, width=800, height=400, bg='white')
UI_frame.grid(row=0, column=0, padx=5, pady=5)

# Escala para los numeros de pares ordenados que vamos a tener
numeroPares = Scale(UI_frame, from_=8, to=12, length=200, digits=1,
                    resolution=1, orient=HORIZONTAL, label="Numero de Pares")
numeroPares.grid(row=0, column=1, padx=5, pady=5)

# Boton para generar los pares ordenados
Button(UI_frame, text="Generar Pares", command=show_plot,
       bg='light green').grid(row=0, column=4, padx=10, pady=10)

# Boton para generar la regresión lineal
Button(UI_frame, text="Regresión Lineal", command='',
       bg='light blue').grid(row=0, column=5, padx=10, pady=10)

# Boton para salir del programa
Button(UI_frame, text="Salir", command=exit, bg='red').grid(
    row=0, column=6, padx=10, pady=10)

root.mainloop()
