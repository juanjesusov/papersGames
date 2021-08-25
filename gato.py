from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

ventanaGato = Tk()
ventanaGato.title("Gato")
ventanaGato.resizable(False, False)
ventanaGato.geometry("1280x720+200+100")
ventanaGato.config(background="grey")
#ventanaGato.iconbitmap("img\icono.ico")

def iniciar():
    for i in range(0,9):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(bg="lightgray")
        listaBotones[i].config(text="")
        listaControl[i] = "N"
    global nombreJugador1, nombreJugador2
    nombreJugador1 = simpledialog.askstring("Jugador","Escribe el nombre del jugador 1:")
    nombreJugador2 = simpledialog.askstring("Jugador","Escribe el nombre del jugador 2:")
    turnoJugador.set("Turno: "+nombreJugador1)

def bloquear():
    for i in range(0,9):
        listaBotones[i].config(state="disable")
        
def cambiar(num):
    global turno, nombreJugador1, nombreJugador2
    if listaControl[num]=="N" and turno==0:
        listaBotones[num].config(text="X")
        listaBotones[num].config(bg="white")
        listaControl[num] = "X"
        turno = 1
        turnoJugador.set("Turno: "+nombreJugador2)
    elif listaControl[num]=="N" and turno==1:
        listaBotones[num].config(text="O")
        listaBotones[num].config(bg="white")
        listaControl[num] = "O"
        turno = 0
        turnoJugador.set("Turno: "+nombreJugador1)
    listaBotones[num].config(state="disable")
    verificar()
    
def verificar():
    if ((listaControl[0]=="X" and listaControl[1]=="X" and listaControl[2]=="X") 
    or (listaControl[3]=="X" and listaControl[4]=="X" and listaControl[5]=="X")
    or (listaControl[6]=="X" and listaControl[7]=="X" and listaControl[8]=="X")
    or (listaControl[0]=="X" and listaControl[3]=="X" and listaControl[6]=="X") 
    or (listaControl[1]=="X" and listaControl[4]=="X" and listaControl[7]=="X")
    or (listaControl[2]=="X" and listaControl[5]=="X" and listaControl[8]=="X")
    or (listaControl[0]=="X" and listaControl[4]=="X" and listaControl[8]=="X")
    or (listaControl[6]=="X" and listaControl[4]=="X" and listaControl[2]=="X")):
        bloquear()
        messagebox.showinfo("Ganador","Ganaste Jugador "+nombreJugador1)
        archivoTexto = open("ganadoresGato.txt","a")
        archivoTexto.write("\n"+nombreJugador1)
        archivoTexto.close()
        
    if ((listaControl[0]=="O" and listaControl[1]=="O" and listaControl[2]=="O") 
    or (listaControl[3]=="O" and listaControl[4]=="O" and listaControl[5]=="O")
    or (listaControl[6]=="O" and listaControl[7]=="O" and listaControl[8]=="O")
    or (listaControl[0]=="O" and listaControl[3]=="O" and listaControl[6]=="O") 
    or (listaControl[1]=="O" and listaControl[4]=="O" and listaControl[7]=="O")
    or (listaControl[2]=="O" and listaControl[5]=="O" and listaControl[8]=="O")
    or (listaControl[0]=="O" and listaControl[4]=="O" and listaControl[8]=="O")
    or (listaControl[6]=="O" and listaControl[4]=="O" and listaControl[2]=="O")):
        bloquear()
        messagebox.showinfo("Ganador","Ganaste Jugador "+nombreJugador2)
        archivoTexto = open("ganadoresGato.txt","a")
        archivoTexto.write("\n"+nombreJugador2)
        archivoTexto.close()
    

turno=0
nombreJugador1 = ""
nombreJugador2 = ""
listaBotones = []
listaControl = [] # Puede contener X, Y o N (que aún está libre)
turnoJugador = StringVar()

for i in range(0,9):
    listaControl.append("N")
    
def atras():
    from PapersGames import index
    
boton0 = Button(ventanaGato, width=9, height=3, command=lambda: cambiar(0))
listaBotones.append(boton0)
boton0.place(x=500, y=200)

boton1 = Button(ventanaGato, width=9, height=3, command=lambda: cambiar(1))
listaBotones.append(boton1)
boton1.place(x=600, y=200)

boton2 = Button(ventanaGato, width=9, height=3, command=lambda: cambiar(2))
listaBotones.append(boton2)
boton2.place(x=700, y=200)

boton3 = Button(ventanaGato, width=9, height=3, command=lambda: cambiar(3))
listaBotones.append(boton3)
boton3.place(x=500, y=300)

boton4 = Button(ventanaGato, width=9, height=3, command=lambda: cambiar(4))
listaBotones.append(boton4)
boton4.place(x=600, y=300)

boton5 = Button(ventanaGato, width=9, height=3, command=lambda: cambiar(5))
listaBotones.append(boton5)
boton5.place(x=700, y=300)

boton6 = Button(ventanaGato, width=9, height=3, command=lambda: cambiar(6))
listaBotones.append(boton6)
boton6.place(x=500, y=400)

boton7 = Button(ventanaGato, width=9, height=3, command=lambda: cambiar(7))
listaBotones.append(boton7)
boton7.place(x=600, y=400)

boton8 = Button(ventanaGato, width=9, height=3, command=lambda: cambiar(8))
listaBotones.append(boton8)
boton8.place(x=700, y=400)

etiquetaTurno = Label(ventanaGato, textvariable=turnoJugador, font=("red,16"), relief="flat").place(x=550, y=100)
iniciar = Button(ventanaGato, text="INICIAR", font=("red,16"), relief="flat", command=iniciar).place(x=600, y=600)

bloquear()

ventanaGato.mainloop()