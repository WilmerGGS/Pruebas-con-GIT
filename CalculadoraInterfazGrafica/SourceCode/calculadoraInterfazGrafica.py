from tkinter import *
import tkinter


#PROGRAMA

ventana = tkinter.Tk()
ventana.geometry("359x400")
ventana.resizable(False,False)
ventana.title("Calculadora")
#ventana.iconbitmap(r"C:\Users\WILMER\Desktop\Proyectos Personales Python\Projects Personal\Archivos terminados Ejecutables\CalculadoraInterfazGrafica\SourceCode\calculator.ico")
ventana.config(bg="#B9B9B9")

#VARIABLES
resultado = ""
operacion = ""
i = 0
porcentaje = ""
resulPorcentaje = ""

#FUNCIONES
def numeroPulsado(valor):
    global i
    pantalla.insert(i, valor)
    i += 1

def borrarTodo():
    global i
    pantalla.delete(0, END)
    i = 0

def hacerOperaciones():
    global i
    operacion = pantalla.get()
    resultado = eval(operacion)
    pantalla.delete(0, END)
    pantalla.insert(0, resultado)

def realizarPorcentajes():
    global porcentaje
    global resultado
    global resulPorcentaje
    porcentaje = pantalla.get()
    resultado = eval(porcentaje)
    pantalla.delete(0, END)
    resulPorcentaje = resultado / 100
    pantalla.insert(0, resulPorcentaje)

#CUADRO TEXTO
pantalla = Entry(ventana, width=12)
pantalla.grid(row=1, column=1, ipadx=111, ipady=25)
pantalla.config(justify="right", bg="Black", fg="White", font=("Arial", 15))

#BOTONES
botonNumero0 = tkinter.Button(ventana, text = "0", width=6, height=4, command= lambda: numeroPulsado("0"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", activeforeground="#070807", relief="flat", overrelief="raised")
botonNumero0.place(x=0, y=320)

botonNumero1 = tkinter.Button(ventana, text = "1", width = 6, height = 4, command= lambda: numeroPulsado("1"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonNumero1.place(x=75, y=320)

botonNumero2 = tkinter.Button(ventana, text = "2", width = 6, height = 4, command= lambda: numeroPulsado("2"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonNumero2.place(x=0, y=240)

botonNumero3 = tkinter.Button(ventana, text = "3", width = 6, height = 4, command= lambda: numeroPulsado("3"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonNumero3.place(x=75, y=240)

botonNumero4 = tkinter.Button(ventana, text = "4", width = 6, height = 4, command= lambda: numeroPulsado("4"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonNumero4.place(x=150, y=240)

botonNumero5 = tkinter.Button(ventana, text = "5", width = 6, height = 4, command= lambda: numeroPulsado("5"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonNumero5.place(x=225, y=240)

botonNumero6 = tkinter.Button(ventana, text = "6", width = 6, height = 4, command= lambda: numeroPulsado("6"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonNumero6.place(x=0, y=160)

botonNumero7 = tkinter.Button(ventana, text = "7", width = 6, height = 4, command= lambda: numeroPulsado("7"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonNumero7.place(x=75, y=160)

botonNumero8 = tkinter.Button(ventana, text = "8", width = 6, height = 4, command= lambda: numeroPulsado("8"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonNumero8.place(x=150, y=160)

botonNumero9 = tkinter.Button(ventana, text = "9", width = 6, height = 4, command= lambda: numeroPulsado("9"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonNumero9.place(x=225, y=160)

botonSuma = tkinter.Button(ventana, text= "+", width= 6, height= 4, command= lambda: numeroPulsado("+"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", activeforeground="#070807", relief="flat", overrelief="raised")
botonSuma.place(x=300, y=320)

botonResta = tkinter.Button(ventana, text= "-", width= 6, height= 4, command= lambda: numeroPulsado("-"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", activeforeground="#070807", relief="flat", overrelief="raised")
botonResta.place(x=300, y=240)

botonMultiplicacion = tkinter.Button(ventana, text= "x", width= 6, height= 4, command= lambda: numeroPulsado("*"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", activeforeground="#070807", relief="flat", overrelief="raised")
botonMultiplicacion.place(x=300, y=160)

botonDivision = tkinter.Button(ventana, text= "÷", width= 6, height= 4, command= lambda: numeroPulsado("/"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", activeforeground="#070807", relief="flat", overrelief="raised")
botonDivision.place(x=300, y=80)

botonParentesisDos = tkinter.Button(ventana, text= ")", width= 6, height= 4, command= lambda: numeroPulsado(")"), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", activeforeground="#070807", relief="flat", overrelief="raised")
botonParentesisDos.place(x=150, y=80)

botonIgual = tkinter.Button(ventana, text = "=", width = 6, height = 4, command= lambda: hacerOperaciones(), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonIgual.place(x=225, y=320)

botonParentesisUno = tkinter.Button(ventana, text= "(", width= 6, height= 4, command= lambda: numeroPulsado("("), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", activeforeground="#070807", relief="flat", overrelief="raised")
botonParentesisUno.place(x=75, y=80)

botonBorrarTodo = tkinter.Button(ventana, text= "C/AC", width= 6, height= 4, command= lambda: borrarTodo(), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", activeforeground="#070807", relief="flat", overrelief="raised")
botonBorrarTodo.place(x=0, y=80)

botonPunto = tkinter.Button(ventana, text= ".", width= 6, height= 4, command= lambda: numeroPulsado("."), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", relief="flat", overrelief="raised")
botonPunto.place(x=150, y=320)

botonPorcentajes = tkinter.Button(ventana, text = "%", width = 6, height = 4, command= lambda: realizarPorcentajes(), font=("Arial", 10), bg="#FFFEFD", activebackground="#D5D5D5", activeforeground="#070807", relief="flat", overrelief="raised")
botonPorcentajes.place(x=225, y=80)

ventana.mainloop()
