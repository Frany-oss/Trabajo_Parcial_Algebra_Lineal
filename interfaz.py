'''
Pida el ingreso de n[8,12] y genere aleatoriamente npares ordenados. 
El programa debemostrar gráficamente la curva que se aproxime mejor linealmente a los npares ordenados. 
El usuario debe seleccionar el tipo de curva: polinomial(de grado 𝑚≤6), exponencial o potencial.
'''
import regresion
import generator
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

# Inicializamos los globales
X = None
Y = None
N = None
V = None

def showPlots():
	global X, Y, N, V

	n = numeroPares.get()
	G = numeroGrado.get()

	# Checkea si X y Y existen o si se pide otra cantidad de pares en el slider
	if n != N:
		N = n
		#0 = desordenado , 1 = ordenado
		X,Y = generator.generateArray(N,1)

	plt.plot(X, Y, 'ro')
	if RegresionMenu.get() == V[0]:
		LR = regresion.linearRegression(X,Y)
		plt.plot(X, LR[0])
		plt.xlabel(LR[1])
	elif RegresionMenu.get() == V[1]:
		PR = regresion.polynominomialRegression(X,Y,G)
		plt.plot(X, PR[0])
		plt.xlabel(PR[1])
	elif RegresionMenu.get() == V[2]:
		PoR = regresion.potentialRegression(X,Y)
		plt.plot(X, PoR[0])
		plt.xlabel(PoR[1])
	elif RegresionMenu.get() == V[3]:
		ER = regresion.exponentialRegression(X,Y)
		plt.plot(X, ER[0])
		plt.xlabel(ER[1])

	plt.title(RegresionMenu.get())
	plt.show()

# --------- INTERFAZ DEL PROGRAMA -----------
root = Tk()
root.title('Regresión Lineal')
root.maxsize(950, 600)
root.geometry('630x200')
root.config(bg='white')

selectRegresion = StringVar()

def exit():
	return root.destroy()

UI_frame = Frame(root, width=800, height=400, bg='white')
UI_frame.grid(row=0, column=0, padx=5, pady=5)

# Escala para los numeros de pares ordenados que vamos a tener
numeroPares = Scale(UI_frame, from_=8, to=12, length=200, digits=1, resolution=1, orient=HORIZONTAL, label="Numero de Pares")
numeroPares.grid(row=0, column=1, padx=5, pady=5)

# Escala para medir el grado polinomial que va desde 2 a 6
numeroGrado = Scale(UI_frame, from_=2, to=6, length=200, digits=1, resolution=1, orient=HORIZONTAL, label="Grado Polinomial")
numeroGrado.grid(row=1, column=1, padx=5, pady=5)

# Boton para generar los pares ordenados
Button(UI_frame, text="Graficar", command=showPlots, bg='light green').grid(row=0, column=4, padx=10, pady=10)

# Boton para salir del programa
Button(UI_frame, text="Salir", command=exit, bg='red').grid(row=0, column=6, padx=10, pady=10)

V = ['Regresión Lineal', 'Regresión Polinomial', 'Regresión Potencial', 'Regresión Exponencial']
RegresionMenu = ttk.Combobox(UI_frame, textvariable=selectRegresion, values=V)
RegresionMenu.current(0)
RegresionMenu.grid(row=0, column=5, padx=3, pady=3)

root.mainloop()