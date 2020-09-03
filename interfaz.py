'''
Pida el ingreso de n[8,12] y genere aleatoriamente npares ordenados. 
El programa debemostrar gráficamente la curva que se aproxime mejor linealmente a los npares ordenados. 
El usuario debe seleccionar el tipo de curva: polinomial(de grado 𝑚≤6), exponencial o potencial.
'''
import regresion
from generator import *
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# Inicializamos los globales
X = None
Y = None
N = None


def show_plots():
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

        # X, Y = generar_pares2(n)
        X.sort()
        X = np.array([X])
        Y = np.array([Y])

    YR = regresion.regresion_lineal(X, Y, n)
    XR2, YR2 = regresion.regresion_polinomial(X, Y, n)
    #regression = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].set_title('Pares Generados')
    axs[0, 0].plot(X[0], Y[0], 'ro')
    axs[0, 1].set_title('Regresión Lineal')
    axs[0, 1].plot(X[0], Y[0], 'ro', X[0], YR[0])
    axs[1, 0].set_title('Regresión Polinomial')
    axs[1, 0].plot(X[0], Y[0], 'ro', XR2[0], YR2[0])
    axs[1, 1].set_title('Regresión exponencial')
    axs[1, 1].plot(X[0], Y[0], 'ro')

    for ax in axs.flat:
        ax.set(xlabel='x', ylabel='y')

# Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.show()


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
Button(UI_frame, text="Generar Pares", command=show_plots,
       bg='light green').grid(row=0, column=4, padx=10, pady=10)


# Boton para salir del programa
Button(UI_frame, text="Salir", command=exit, bg='red').grid(
    row=0, column=6, padx=10, pady=10)

root.mainloop()
