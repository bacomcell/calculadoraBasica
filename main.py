from tkinter import*
import math

menu = Tk()
menu.title("Calculadora")
menu.resizable(0,0)

i = 0
#entrada de texto
v = Entry(menu, width=30, borderwidth=10)  
v.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

def click_button(valor):
    global i
    v.insert(i, valor)
    i += 1

def borrar():
    v.delete(0, END)
    i = 0   
    
def hacer_operacion():
    ecuacion = v.get()
    resultado = eval(ecuacion)
    v.delete(0, END)
    v.insert(0, resultado)
    i = 0 


#botones 
boton1 = Button(menu, text="1", width=5, height=2, command= lambda: click_button(1))
boton2 = Button(menu, text="2", width=5, height=2, command= lambda: click_button(2))
boton3 = Button(menu, text="3", width=5, height=2, command= lambda: click_button(3))
boton4 = Button(menu, text="4", width=5, height=2, command= lambda: click_button(4))
boton5 = Button(menu, text="5", width=5, height=2, command= lambda: click_button(5))
boton6 = Button(menu, text="6", width=5, height=2, command= lambda: click_button(6))
boton7 = Button(menu, text="7", width=5, height=2, command= lambda: click_button(7))
boton8 = Button(menu, text="8", width=5, height=2, command= lambda: click_button(8))
boton9 = Button(menu, text="9", width=5, height=2, command= lambda: click_button(9))
boton0 = Button(menu, text="0", width=13, height=2, command= lambda: click_button(0))

boton_borrar = Button(menu, text="AC", width=5, height=2, command= lambda: borrar())
boton_parentesis1 = Button(menu, text=")", width=5, height=2, command= lambda: click_button(")"))
boton_parentesis2 = Button(menu, text="(", width=5, height=2, command= lambda: click_button("("))
boton_punto = Button(menu, text=".", width=5, height=2, command= lambda: click_button("."))

boton_div = Button(menu, text="÷", width=5, height=2, command= lambda: click_button("/"))
boton_mult = Button(menu, text="x", width=5, height=2, command= lambda: click_button("*"))
boton_sum = Button(menu, text="+", width=5, height=2, command= lambda: click_button("+"))
boton_rest = Button(menu, text="-", width=5, height=2, command= lambda: click_button("-"))
boton_igual = Button(menu, text="=↑", width=5, height=2, command= lambda: hacer_operacion())

#agregar botones en pantalla
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=2, padx=5, pady=5)
boton_rest.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_sum.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_div.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_mult.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)


menu.mainloop()
