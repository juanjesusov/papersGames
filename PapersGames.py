from tkinter import  *
import tkinter as tk
from PIL import ImageTk, Image
import sys
import random
from io import open
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------Indice--------------------------------------
def index():    
    ventanaIndice = tk.Tk()
    ventanaIndice.title("Paper´s Games")
    ventanaIndice.resizable(False, False)
    ventanaIndice.geometry("1280x720+200+100")
    #ventanaIndice.configure(background=img)
    #ventanaIndice.iconbitmap("img\icono.ico")
    
    img = PhotoImage(file="bgIndex.png")
    bg_label = Label(ventanaIndice, image=img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.pack()
    
    btnImgGato = PhotoImage(file="gatoIcono.png")
    btnImgAhorcado = PhotoImage(file="ahorcadoIcono.png")
            
    botonInfoGeneral = tk.Button(ventanaIndice, text="Info", font=("red,16"), relief="flat", command=infoGeneral)
    botonInfoGeneral.place(x=1200, y=650)
    
    botonGato = tk.Button(ventanaIndice, image=btnImgGato, command=gato)
    botonGato.place(x=300, y=300)
    
    botonAhorcado = tk.Button(ventanaIndice, image=btnImgAhorcado, command=ahorcado)
    botonAhorcado.place(x=600, y=300)
    
    botonSalir = tk.Button(ventanaIndice, text="SALIR", font=("red,16"), relief="flat", command=salir)
    botonSalir.place(x=20, y=650)
    
    botonGanadores = tk.Button(ventanaIndice, text="GANADORES", font=("red,16"), relief="flat", command=ganadores)
    botonGanadores.place(x=1100, y=20)
    
    ventanaIndice.mainloop()

def salir():
    pass

def ganadores():
    ventanaGanadores = tk.Tk()
    ventanaGanadores.title("Ganadores")
    ventanaGanadores.resizable(False, False)
    ventanaGanadores.geometry("1280x720+200+100")
    ventanaGanadores.config(background="grey")
    #ventanaGanadores.iconbitmap("img\icono.ico")

    texto2 = tk.Label(ventanaGanadores, text="Cerrar ventana para regresar al menú, y ver gráficas", font=("red, 16"))
    texto2.place(x=20, y=600)
    
    titulo = tk.Label(ventanaGanadores, text="GANADORES", font=("red, 24"))
    titulo.place(x=10, y=10)
    
    subt1 = tk.Label(ventanaGanadores, text="Gato\n(En consola)", font=("red, 20"))
    subt1.place(x=10, y=100)
    
    subt2 = tk.Label(ventanaGanadores, text="Ahorcado\n(En consola)", font=("red, 20"))
    subt2.place(x=10, y=300)
    
    print("\t\tGANADORES\n\n")
    
    archivo_texto_gato = open("ganadoresGato.txt","r")
    textoGato = archivo_texto_gato.read()
    archivo_texto_gato.close()
    print("\tGato\n"+textoGato+"\n")
    
    archivo_texto_ahorcado = open("ganadoresAhorcado.txt","r")
    textoAhorcado = archivo_texto_ahorcado.read()
    archivo_texto_ahorcado.close()
    print("\tAhorcado\n"+textoAhorcado+"\n")
    
    archivoTextoGato = open("ganadoresGato.txt","r").read().split('\n')
    serieGato = pd.Series(archivoTextoGato)
    nivelesG = serieGato.value_counts()
    plt.figure()
    plt.title('Gato')
    nivelesG.plot(kind='bar')
    plt.legend(loc='best')
    plt.show()
    #archivoTextoGato.close()
    
    archivoTextoAhorcado = open("ganadoresAhorcado.txt","r").read().split('\n')
    serieAhorcado = pd.Series(archivoTextoAhorcado)
    nivelesA = serieAhorcado.value_counts()
    plt.figure()
    plt.title('Ahorcado')
    nivelesA.plot(kind='bar')
    plt.legend(loc='best')
    plt.show()
    #archivoTextoGato.close()
    
    
    ventanaGanadores.mainloop()
    
#--------------------------Funciones de información---------------------------
def infoGeneral():
    ventanaInfoGeneral = tk.Tk()
    ventanaInfoGeneral.title("Información General")
    ventanaInfoGeneral.resizable(False, False)
    ventanaInfoGeneral.geometry("1280x720+200+100")
    ventanaInfoGeneral.config(background="grey")
    #ventanaInfoGeneral.iconbitmap("img\icono.ico")
    
    titulo = tk.Label(ventanaInfoGeneral, text="INFORMACIÓN GENERAL", font=("red, 24"))
    titulo.place(x=10, y=10)
    
    texto = tk.Label(ventanaInfoGeneral, text="Bienvenido a Paper´s Game es un juego con el objetivo de entretener a las personas \ny puedan desarrollar habilidades de lógica, estrategia, etc... \n\nPásalo genial!!", font=("red, 18"))
    texto.place(x=80, y=100)
    
    texto2 = tk.Label(ventanaInfoGeneral, text="Cerrar ventana para regresar al menú", font=("red, 16"))
    texto2.place(x=20, y=600)
    
    ventanaInfoGeneral.mainloop()

def infoGato():
    ventanaInfoGato = tk.Tk()
    ventanaInfoGato.title("Información sobre el juego \"Gato\"")
    ventanaInfoGato.resizable(False, False)
    ventanaInfoGato.geometry("1280x720+200+100")
    ventanaInfoGato.config(background="grey")
    #ventanaInfoGato.iconbitmap("img\icono.ico")

    botonAtras = tk.Button(ventanaInfoGato, text="<-", font=("red,16"), relief="flat", command=gato)
    botonAtras.place(x=20, y=650)
    
    titulo = tk.Label(ventanaInfoGato, text="INFORMACIÓN SOBRE EL JUEGO \"GATO\"", font=("red, 24"))
    titulo.place(x=10, y=10)
    
    texto = tk.Label(ventanaInfoGato, text="El juego del gato es un juego que se creó hace décadas con el propósito de concluir \nrivalidades entre dos jugadores. Al inicio del juego se tendrá que presionar \nel botón de \"Iniciar\", ambos jugadores tendrán que elegir entre unos de los \n9 campos a través de turnos, al finalizar aparecerá el ganador.", font=("red, 18"))
    texto.place(x=80, y=100)
    
    ventanaInfoGato.mainloop()
    
def infoAhorcado():
    ventanaInfoAhorcado = tk.Tk()
    ventanaInfoAhorcado.title("Información sobre el juego \"Ahorcado\"")
    ventanaInfoAhorcado.resizable(False, False)
    ventanaInfoAhorcado.geometry("1280x720+200+100")
    ventanaInfoAhorcado.config(background="grey")
    #ventanaInfoAhorcado.iconbitmap("img\icono.ico")

    botonAtras = tk.Button(ventanaInfoAhorcado, text="<-", font=("red,16"), relief="flat", command=ahorcado)
    botonAtras.place(x=20, y=650)
    
    titulo = tk.Label(ventanaInfoAhorcado, text="INFORMACIÓN SOBRE EL JUEGO \"AHORCADO\"", font=("red, 24"))
    titulo.place(x=10, y=10)
    
    texto = tk.Label(ventanaInfoAhorcado, text="El ahorcado es un juego didáctico que desarrolla habilidades de pensamiento por \nlos usuarios al generar cierta hipótesis cuando se trata de acertar el tipo \nde palabra que se crea en el tablero. Para el juego del ahorcado se obtendrá una palabra \na partir de alrededor de 500, que lanzará una el propio sistema, se \ndeberá escribir una letra como participación y mientras no se hacerte una letra \nserá una oportunidad perdida, al final lanzará el resultado de la partida, y si \nes necesario, la palabra correcta.", font=("red, 18"))
    texto.place(x=50, y=100)
    
    ventanaInfoAhorcado.mainloop()
    
#--------------------------Juegos---------------------------
def gato():
    ventanaGato = tk.Tk()
    ventanaGato.title("Gato")
    ventanaGato.resizable(False, False)
    ventanaGato.geometry("1280x720+200+100")
    ventanaGato.config(background="grey")
    #ventanaGato.iconbitmap("img\icono.ico")
    
    texto2 = tk.Label(ventanaGato, text="Cerrar ventana para regresar al menú", font=("red, 16"))
    texto2.place(x=20, y=600)
    
    botonInfoGato = tk.Button(ventanaGato, text="Info", font=("red,16"), relief="flat", command=infoGato)
    botonInfoGato.place(x=1200, y=650)
    
    botonEmpezar = tk.Button(ventanaGato, text="Empezar", font=("red,16"), relief="flat", command=gatoJuego)
    botonEmpezar.place(x=300, y=300)

    ventanaGato.mainloop()

def gatoJuego():
    import gato

    
def ahorcado():
    ventanaAhorcado = tk.Tk()
    ventanaAhorcado.title("Ahorcado")
    ventanaAhorcado.resizable(False, False)
    ventanaAhorcado.geometry("1280x720+200+100")
    ventanaAhorcado.config(background="grey")
    #ventanaAhorcado.iconbitmap("img\icono.ico")
    
    texto2 = tk.Label(ventanaAhorcado, text="Cerrar ventana para regresar al menú", font=("red, 16"))
    texto2.place(x=20, y=600)
    
    botonInfoAhorcado = tk.Button(ventanaAhorcado, text="Info", font=("red,16"), relief="flat", command=infoAhorcado)
    botonInfoAhorcado.place(x=1200, y=650)
    
    textoInstruccion = tk.Label(ventanaAhorcado, text="Dirigete a tu consola para comenzar!!", font=("red, 20"))
    textoInstruccion.place(x=250, y=250)
    
    botonEmpezar = tk.Button(ventanaAhorcado, text="Empezar", font=("red,16"), relief="flat", command=ahorcadoJuego)
    botonEmpezar.place(x=300, y=300)
    
    ventanaAhorcado.mainloop()
    
def ahorcadoJuego():
    import ahorcado
    
#-------------------------------------Inicio----------------------------------

index()
