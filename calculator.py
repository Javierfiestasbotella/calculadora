from tkinter import *
raiz=Tk()
miframe=Frame(raiz,width=650, height=600,background="white")
miframe.pack()
operacion=""
resultado=0
#-------------------pantalla----------
numeroPantalla=StringVar()

pantalla=Entry(miframe,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)#colunspan hace que salga alineados los botones. Bueno hace que la pantalla ocupe mas columnas no solo 1 asi no arrastra las demas
pantalla.config(background="black",fg="#03f943",justify="right")#la pantalla donde van los numeros es negra se escribe con color verde y a la derecha

#---------------pulsaciones teclado---------

def numeroPulsado(num):
    global operacion
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get()+ num)

#--------------funcion suma-----

def suma(num):
    global operacion
    global resultado
    resultado+=float(num)#incrementa a resultado el numero entero que hay en pantalla
    operacion="suma"
    numeroPantalla.set(resultado)# esto hace que cada vez que demos al + vaya apareciendo los numeros sumados anteriores
#--------funcion resta------

def resta(num):
    global operacion
    global resultado
    resultado-=float(num)
    operacion="resta"
    numeroPantalla.set(resultado)

#----------Multiplicar------
def multi (num):
    global operacion
    global ressultado
    resultado=resultado*resultado

#-------funcio el resultado-------

def el_resultado():
    global resultado

    numeroPantalla.set(resultado+float(numeroPantalla.get()))
    resultado=0

#-------fila1--------------
boton7=Button(miframe,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miframe,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miframe,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonMult=Button(miframe,text="x",width=3,command=lambda:numeroPulsado("x"))
botonMult.grid(row=2,column=4)

#----------------fila2--------
boton4=Button(miframe,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miframe,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miframe,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonDiv=Button(miframe,text="÷",width=3,command=lambda:numeroPulsado("÷"))
botonDiv.grid(row=3,column=4)

#-------------------------fila3-----
boton1=Button(miframe,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miframe,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miframe,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonSum=Button(miframe,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=4,column=4)

#-------------------------fila4---
botonDec=Button(miframe,text=",",width=3,command=lambda:numeroPulsado(","))
botonDec.grid(row=5,column=1)
boton0=Button(miframe,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=2)
botonIgual=Button(miframe,text="=",width=3,command=lambda:el_resultado())
botonIgual.grid(row=5,column=3)
botonRest=Button(miframe,text="-",width=3,command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=5,column=4)


#milabel=Label(miframe,text="\n Este es mi primer texto",fg="white",bg="green",font=("courier",15))
#milabel.pack()
#milabel.place(x=125,y=125)
#milogo=PhotoImage(file="img.png")
#Label(miframe,img=milogo).place(x=130,y=145)



raiz.mainloop()