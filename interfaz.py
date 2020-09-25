'''
Pida el ingreso de n[8,12] y genere aleatoriamente npares ordenados. 
El programa debemostrar gráficamente la curva que se aproxime mejor linealmente a los npares ordenados. 
El usuario debe seleccionar el tipo de curva: polinomial(de grado 𝑚≤6), exponencial o potencial.
'''
import regresion
import generator
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy

# Inicializamos los globales
X = None
Y = None
N = None
O = None

# Mostrar el grafico


def showPlots():
    global X, Y, N, O
    n = numeroPares.get()
    o = check.get()
    G = numeroGrado.get()
    X_n = numpy.arange(1, 25, 0.1)
    # Revisa si X y Y existen o si se pide otra cantidad de pares en el slider
    if n != N or o != O:
        N = n
        O = o
        X, Y = generator.generateArray(N, O)

    if not plt.get_fignums():
        plt.figure(figsize=(9, 5))
        plt.plot(X, Y, 'ro')
    if RegresionMenu.get() == V[0]:
        LR = regresion.linearRegression(X, Y)
        plt.plot(X, LR[0], label=RegresionMenu.get())
        plt.title(LR[1])
    elif RegresionMenu.get() == V[1]:
        PR = regresion.polynominomialRegression(X, Y, G)
        titulo = RegresionMenu.get() + " (Grado " + str(G) + ")"
        plt.plot(X_n, PR[0], label=titulo)
        plt.title(PR[1])
    elif RegresionMenu.get() == V[2]:
        PoR = regresion.potentialRegression(X, Y)
        plt.plot(X_n, PoR[0], label=RegresionMenu.get())
        plt.title(PoR[1])
    elif RegresionMenu.get() == V[3]:
        ER = regresion.exponentialRegression(X, Y)
        plt.plot(X_n, ER[0], label=RegresionMenu.get())
        plt.title(ER[1])

    plt.xlabel("X")
    plt.ylabel("Y")
    # plt.title(RegresionMenu.get())
    plt.legend()
    plt.show()


# --------- INTERFAZ DEL PROGRAMA -----------
root = tk.Tk()
root.title('Regresión Lineal')
root.maxsize(950, 600)
root.geometry('500x150')
root.config(bg='white')

selectRegresion = tk.StringVar()


def exit():
    return root.destroy()


UI_frame = tk.Frame(root, width=800, height=400, bg='white')
UI_frame.grid(row=0, column=0, padx=5, pady=5)

# Escala para los numeros de pares ordenados que vamos a tener
numeroPares = tk.Scale(UI_frame, from_=8, to=12, length=200, digits=1,
                       resolution=1, orient=tk.HORIZONTAL, label="Numero de Pares")
numeroPares.grid(row=0, column=1, padx=5, pady=5)

# Escala para medir el grado polinomial que va desde 2 a 6
numeroGrado = tk.Scale(UI_frame, from_=2, to=6, length=200, digits=1,
                       resolution=1, orient=tk.HORIZONTAL, label="Grado Polinomial")
numeroGrado.grid(row=1, column=1, padx=5, pady=5)

# Checkbox para ordenar los pares del Y
check = tk.IntVar()  # (value=0)
ordenado = tk.Checkbutton(UI_frame, text="Ordenado", variable=check)
ordenado.place(x=127, y=5)
ordenado.select()

# Boton para generar los pares ordenados
tk.Button(UI_frame, text="Graficar", command=showPlots,
          bg='light green').grid(row=0, column=4, padx=10, pady=10)

# Boton para salir del programa
tk.Button(UI_frame, text="Salir", command=exit, bg='red').grid(
    row=0, column=6, padx=10, pady=10)

V = ['Regresión Lineal', 'Regresión Polinomial',
     'Regresión Potencial', 'Regresión Exponencial']
RegresionMenu = ttk.Combobox(UI_frame, textvariable=selectRegresion, values=V)
RegresionMenu.current(0)
RegresionMenu.grid(row=0, column=5, padx=3, pady=3)

root.mainloop()
