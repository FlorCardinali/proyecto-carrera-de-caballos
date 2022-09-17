#Programa: Carrera de caballos.
#Autores: Flor Cardinali - Fran Cuschie.
#Emails: florenciapaulacardinali@gmail.com / francuschie@gmail.com .
#Fecha: 28/6/2022.

import random
from os import system




def MezclarCartas(Cartas):
    longitud = len(Cartas)
    for i in range(longitud):
        indiceRandom = random.randint(0, longitud-1)
        temporal = Cartas[i]
        Cartas[i] = Cartas[indiceRandom]
        Cartas[indiceRandom] = temporal
    return Cartas
#Reglas del juego
def Reglas ():
    print ("--------------------------------------------")
    print ("|            Reglas basicas:               |")
    print ("|                                          |")   
    print ("| 1. Se colocan 11 cartas aleatorias boca  |")
    print ("| abajo en una linea horizontal.           |")
    print ("| 2. Los 4 jugadores eligen un caballo y   |")
    print ("| los colocan en una linea horizantal      |")
    print ("| abajo y a la izquierda de la columna de  |")
    print ("| cartas boca abajo.                       |")
    print ("| 3. Se iran tirando cartas del mazo       |")
    print ("| restante y los caballos avanzaran 1      |")
    print ("| espacio cuando estas cartas coincidan    |")
    print ("| con su palo.                             |")
    print ("| 4. Por ultimo, cuando todos los caballos |")
    print ("| hallan abandonado la linea horizantal    |")
    print ("| delimitada por cada una de las cartas de |")
    print ("| la columna, esta carta se gira y su palo |")
    print ("| determina quien retrocede un espacio.    |")
    print ("--------------------------------------------")
#Dibujado de tablero
def caballos(ContadorBasto,ContadorCopa,ContadorOro,ContadorEspada,EvPos):
    #Control de cartas Boca abajo
    if EvPos == 1:
        print("   █  █  █  █  █  █  █  █  █  █  █")
    elif EvPos == 2:
        print("      █  █  █  █  █  █  █  █  █  █")
    elif EvPos == 3:
        print("         █  █  █  █  █  █  █  █  █")
    elif EvPos == 4:
        print("            █  █  █  █  █  █  █  █")
    elif EvPos == 5:
        print("               █  █  █  █  █  █  █")
    elif EvPos == 6:
        print("                  █  █  █  █  █  █")
    elif EvPos == 7:
        print("                     █  █  █  █  █")
    elif EvPos == 8:
        print("                        █  █  █  █")
    elif EvPos == 9:
        print("                           █  █  █")
    elif EvPos == 10:
        print("                              █  █")
    elif EvPos == 11:
        print("                                 █")

    #Estados del caballo de Espada
    if ContadorEspada == 0:
        print("\033[;34m"+"E "+"\033[0;m"+" _  _  _  _  _  _  _  _  _  _  _  |_")
    elif ContadorEspada == 1:
        print("_ "+"\033[;34m"+" E "+"\033[0;m"+" _  _  _  _  _  _  _  _  _  _  |_")
    elif ContadorEspada == 2:
        print("_  _ "+"\033[;34m"+" E "+"\033[0;m"+" _  _  _  _  _  _  _  _  _  |_")
    elif ContadorEspada == 3:
        print("_  _  _ "+"\033[;34m"+" E "+"\033[0;m"+" _  _  _  _  _  _  _  _  |_")
    elif ContadorEspada == 4:
        print("_  _  _  _ "+"\033[;34m"+" E "+"\033[0;m"+" _  _  _  _  _  _  _  |_")
    elif ContadorEspada == 5:
        print("_  _  _  _  _ "+"\033[;34m"+" E "+"\033[0;m"+" _  _  _  _  _  _  |_")
    elif ContadorEspada == 6:
        print("_  _  _  _  _  _ "+"\033[;34m"+" E "+"\033[0;m"+" _  _  _  _  _  |_")
    elif ContadorEspada == 7:
        print("_  _  _  _  _  _  _ "+"\033[;34m"+" E "+"\033[0;m"+" _  _  _  _  |_")
    elif ContadorEspada == 8:
        print("_  _  _  _  _  _  _  _ "+"\033[;34m"+" E "+"\033[0;m"+" _  _  _  |_")
    elif ContadorEspada == 9:
        print("_  _  _  _  _  _  _  _  _ "+"\033[;34m"+" E "+"\033[0;m"+" _  _  |_")
    elif ContadorEspada == 10:
        print("_  _  _  _  _  _  _  _  _  _ "+"\033[;34m"+" E "+"\033[0;m"+" _  |_")
    elif ContadorEspada == 11:
        print("_  _  _  _  _  _  _  _  _  _  _ "+"\033[;34m"+" E "+"\033[0;m"+" |_")
    elif ContadorEspada == 12:
        print("_  _  _  _  _  _  _  _  _  _  _  _  |"+"\033[;34m"+" E "+"\033[0;m")
    #Estados del caballo de Basto
    if ContadorBasto == 0:
        print("\033[;32m"+"B "+"\033[0;m"+ " _  _  _  _  _  _  _  _  _  _  _  |_")
    elif ContadorBasto == 1:
        print("_ "+"\033[;32m"+" B "+"\033[0;m"+ " _  _  _  _  _  _  _  _  _  _  |_")
    elif ContadorBasto == 2:
        print("_  _ "+"\033[;32m"+" B "+"\033[0;m"+ " _  _  _  _  _  _  _  _  _  |_")
    elif ContadorBasto == 3:
        print("_  _  _ "+"\033[;32m"+" B "+"\033[0;m"+ " _  _  _  _  _  _  _  _  |_")
    elif ContadorBasto == 4:
        print("_  _  _  _ "+"\033[;32m"+" B "+"\033[0;m"+ " _  _  _  _  _  _  _  |_")
    elif ContadorBasto == 5:
        print("_  _  _  _  _ "+"\033[;32m"+" B "+"\033[0;m"+ " _  _  _  _  _  _  |_")
    elif ContadorBasto == 6:
        print("_  _  _  _  _  _ "+"\033[;32m"+" B "+"\033[0;m"+ " _  _  _  _  _  |_")
    elif ContadorBasto == 7:
        print("_  _  _  _  _  _  _ "+"\033[;32m"+" B "+"\033[0;m"+ " _  _  _  _  |_")
    elif ContadorBasto == 8:
        print("_  _  _  _  _  _  _  _ "+"\033[;32m"+" B "+"\033[0;m"+ " _  _  _  |_")
    elif ContadorBasto == 9:
        print("_  _  _  _  _  _  _  _  _ "+"\033[;32m"+" B "+"\033[0;m"+ " _  _  |_")
    elif ContadorBasto == 10:
        print("_  _  _  _  _  _  _  _  _  _ "+"\033[;32m"+" B "+"\033[0;m"+ " _  |_")
    elif ContadorBasto == 11:
        print("_  _  _  _  _  _  _  _  _  _  _ "+"\033[;32m"+" B "+"\033[0;m"+ " |_")
    elif ContadorBasto == 12:
        print("_  _  _  _  _  _  _  _  _  _  _  _  |"+"\033[;32m"+" B "+"\033[0;m")
    #Estado del caballo de Copa
    if ContadorCopa == 0:
        print("\033[;31m"+"C "+"\033[0;m"+" _  _  _  _  _  _  _  _  _  _  _  |_")
    elif ContadorCopa == 1:
        print("_ " + "\033[;31m"+" C "+"\033[0;m"+" _  _  _  _  _  _  _  _  _  _  |_")
    elif ContadorCopa == 2:
        print("_  _ "+"\033[;31m"+" C "+"\033[0;m"+" _  _  _  _  _  _  _  _  _  |_")
    elif ContadorCopa == 3:
        print("_  _  _ "+"\033[;31m"+" C "+"\033[0;m"+" _  _  _  _  _  _  _  _  |_")
    elif ContadorCopa == 4:
        print("_  _  _  _ "+"\033[;31m"+" C "+"\033[0;m"+" _  _  _  _  _  _  _  |_")
    elif ContadorCopa == 5:
        print("_  _  _  _  _ "+"\033[;31m"+" C "+"\033[0;m"+" _  _  _  _  _  _  |_")
    elif ContadorCopa == 6:
        print("_  _  _  _  _  _ "+"\033[;31m"+" C "+"\033[0;m"+" _  _  _  _  _  |_")
    elif ContadorCopa == 7:
        print("_  _  _  _  _  _  _ "+"\033[;31m"+" C "+"\033[0;m"+" _  _  _  _  |_")
    elif ContadorCopa == 8:
        print("_  _  _  _  _  _  _  _ "+"\033[;31m"+" C "+"\033[0;m"+" _  _  _  |_")
    elif ContadorCopa == 9:
        print("_  _  _  _  _  _  _  _  _ "+"\033[;31m"+" C "+"\033[0;m"+" _  _  |_")
    elif ContadorCopa == 10:
        print("_  _  _  _  _  _  _  _  _  _ "+"\033[;31m"+" C "+"\033[0;m"+" _  |_")
    elif ContadorCopa == 11:
        print("_  _  _  _  _  _  _  _  _  _  _ "+"\033[;31m"+" C "+"\033[0;m"+" |_")
    elif ContadorCopa == 12:
        print("_  _  _  _  _  _  _  _  _  _  _  _  |"+"\033[;31m"+"C "+"\033[0;m")
    #Estado del caballo de Oro
    if ContadorOro == 0:
        print("\033[;33m"+"O "+"\033[0;m"+" _  _  _  _  _  _  _  _  _  _  _  |_")
    elif ContadorOro == 1:
        print("_ "+"\033[;33m"+" O "+"\033[0;m"+" _  _  _  _  _  _  _  _  _  _  |_")
    elif ContadorOro == 2:
        print("_  _ "+"\033[;33m"+" O "+"\033[0;m"+" _  _  _  _  _  _  _  _  _  |_")
    elif ContadorOro == 3:
        print("_  _  _ "+"\033[;33m"+" O "+"\033[0;m"+" _  _  _  _  _  _  _  _  |_")
    elif ContadorOro == 4:
        print("_  _  _  _ "+"\033[;33m"+" O "+"\033[0;m"+" _  _  _  _  _  _  _  |_")
    elif ContadorOro == 5:
        print("_  _  _  _  _ "+"\033[;33m"+" O "+"\033[0;m"+" _  _  _  _  _  _  |_")
    elif ContadorOro == 6:
        print("_  _  _  _  _  _ "+"\033[;33m"+" O "+"\033[0;m"+" _  _  _  _  _  |_")
    elif ContadorOro == 7:
        print("_  _  _  _  _  _  _ "+"\033[;33m"+" O "+"\033[0;m"+" _  _  _  _  |_")
    elif ContadorOro == 8:
        print("_  _  _  _  _  _  _  _ "+"\033[;33m"+" O "+"\033[0;m"+" _  _  _  |_")
    elif ContadorOro == 9:
        print("_  _  _  _  _  _  _  _  _ "+"\033[;33m"+" O "+"\033[0;m"+" _  _  |_")
    elif ContadorOro == 10:
        print("_  _  _  _  _  _  _  _  _  _ "+"\033[;33m"+" O "+"\033[0;m"+" _  |_")
    elif ContadorOro == 11:
        print("_  _  _  _  _  _  _  _  _  _  _ "+"\033[;33m"+" O "+"\033[0;m"+" |_")
    elif ContadorOro == 12:
        print("_  _  _  _  _  _  _  _  _  _  _  _  |"+"\033[;33m"+"O "+"\033[0;m")

#Nazo De Cartas
MazoDeCartas = [
    {'nombre' : "Uno de Basto", "palo": "basto"},
    {'nombre' : "Dos de Basto","palo" : "basto"}, 
    {'nombre' : "Tres de Basto","palo" : "basto"}, 
    {'nombre' : "Cuatro de Basto","palo" : "basto"}, 
    {'nombre' : "Cinco de Basto","palo" : "basto"}, 
    {'nombre' : "Seis de Basto","palo" : "basto"}, 
    {'nombre' : "Siete de Basto","palo" : "basto"}, 
    {'nombre' : "Ocho de Basto","palo" : "basto"}, 
    {'nombre' : "Nueve de Basto", "palo" : "basto"}, 
    {'nombre' : "Diez de basto","palo": "basto"}, 
    {'nombre' : "Doce de Basto","palo": "basto"},
    {'nombre' : "Uno de Copa", "palo": "copa"},
    {'nombre' : "Dos de Copa","palo" : "copa"}, 
    {'nombre' : "Tres de Copa","palo" : "copa"}, 
    {'nombre' : "Cuatro de Copa","palo" : "copa"}, 
    {'nombre' : "Cinco de Copa","palo" : "copa"}, 
    {'nombre' : "Seis de Copa","palo" : "copa"}, 
    {'nombre' : "Siete de Copa","palo" : "copa"}, 
    {'nombre' : "Ocho de Copa","palo" : "copa"}, 
    {'nombre' : "Nueve de Copa", "palo" : "copa"}, 
    {'nombre' : "Diez de Copa","palo": "copa"}, 
    {'nombre' : "Doce de Copa","palo": "copa"}, 
    {'nombre' : "Uno de Oro", "palo": "oro"},
    {'nombre' : "Dos de Oro","palo" : "oro"}, 
    {'nombre' : "Tres de Oro","palo" : "oro"}, 
    {'nombre' : "Cuatro de Oro","palo" : "oro"}, 
    {'nombre' : "Cinco de Oro","palo" : "oro"}, 
    {'nombre' : "Seis de Oro","palo" : "oro"}, 
    {'nombre' : "Siete de Oro","palo" : "oro"}, 
    {'nombre' : "Ocho de Oro","palo" : "oro"}, 
    {'nombre' : "Nueve de Oro", "palo" : "oro"}, 
    {'nombre' : "Diez de Oro","palo": "oro"}, 
    {'nombre' : "Doce de Oro","palo": "oro"},
    {'nombre' : "Uno de Espada", "palo": "espada"},
    {'nombre' : "Dos de Espada","palo" : "espada"}, 
    {'nombre' : "Tres de Espada","palo" : "espada"}, 
    {'nombre' : "Cuatro de Espada","palo" : "espada"}, 
    {'nombre' : "Cinco de Espada","palo" : "espada"}, 
    {'nombre' : "Seis de Espada","palo" : "espada"}, 
    {'nombre' : "Siete de Espada","palo" : "espada"}, 
    {'nombre' : "Ocho de Espada","palo" : "espada"}, 
    {'nombre' : "Nueve de Espada", "palo" : "espada"}, 
    {'nombre' : "Diez de Espada","palo": "espada"}, 
    {'nombre' : "Doce de Espada","palo": "espada"}]

#Presentacion
while True:

    print ("-----------------------------------")
    print ("|                                 |")
    print ("|    Bienvenidos a la carrera     |")
    print ("|     mas emocionante de sus      |")
    print ("|             vidas!!!            |")
    print ("|                                 |")
    print ("-----------------------------------")
    print ("|             1. Jugar            |")
    print ("|             2. Salir            |")
    print ("-----------------------------------")
    #Cuerpo del menu 
    respuesta = int(input())
    if respuesta == 1:
        #Estetica Del Programa
        system("cls")
        Reglas()
        input()
        system("cls")

        #Creacion de Cartas
        CartasBocaAbajo = []
        CartasJugables = []
        for i in range(0,44):
            CartasJugables.append(MazoDeCartas[i])
        for i in range(0,11):
            end = False
            while end == False:
                indice = random.randint(0, 43)
                if MazoDeCartas[indice] in CartasBocaAbajo:
                    continue
                else: 
                    CartasBocaAbajo.append(MazoDeCartas[indice])
                    end = True
            CartasJugables[indice] = 0

        #mezclar cartas
        CartasJugables = MezclarCartas(CartasJugables)
    
        #Contador de indice de Cartas Jugables
        ContIndices = 0
        #contadores de "puntos" de los caballos
        ContadorEspada = 0
        ContadorBasto = 0
        ContadorOro = 0
        ContadorCopa = 0
        #contador para evaluar las cartas boca abajo
        EvPos = 1
        
        #print(CartasJugables)
        while True:
            #comprobador de ceros
            if ContIndices < 43:
                while CartasJugables[ContIndices] == 0:
                    ContIndices = ContIndices + 1
            else:
                ContIndices = 0
                CartasJugables = MezclarCartas(CartasJugables)   
                while CartasJugables[ContIndices] == 0:
                    ContIndices = ContIndices + 1
            
            
            #Aumento de puntos de los caballos
            print("-----------------------------------")
            print("               Carta:              ")
            print("  "+ CartasJugables[ContIndices]['nombre'])
            if CartasJugables[ContIndices]["palo"] == "espada":
                ContadorEspada = ContadorEspada + 1
                print("-----------------------------------")
                print ("Avanza el caballo de "+"\033[;34m"+"Espada!!!"+"\033[0;m")
                print("-----------------------------------")
            elif CartasJugables[ContIndices]["palo"] == "basto": 
                ContadorBasto = ContadorBasto + 1
                print("-----------------------------------")
                print ("Avanza el caballo de "+"\033[;32m"+"Basto!!!"+"\033[0;m")
                print("-----------------------------------")
            elif CartasJugables[ContIndices]["palo"] == "oro":   
                ContadorOro = ContadorOro + 1
                print("-----------------------------------")
                print ("Avanza el caballo de "+"\033[;33m"+"Oro!!!"+"\033[0;m")
                print("-----------------------------------")
            elif CartasJugables[ContIndices]["palo"] == "copa": 
                ContadorCopa = ContadorCopa + 1
                print("-----------------------------------")
                print ("Avanza el caballo de "+"\033[;31m"+"Copas!!!"+"\033[0;m")
                print("-----------------------------------")

            #Aumento de indices del mmazo de jugables
            ContIndices = ContIndices + 1

            #Condicion de "Carta develada"
            if (ContadorEspada > EvPos) and (ContadorOro > EvPos):
                if (ContadorBasto > EvPos) and (ContadorCopa > EvPos):
                    print ("Se da vuelta una carta boca abajo...")
                    print ("Era el " + CartasBocaAbajo[-1]["nombre"])
                    EvPos = EvPos + 1
                    if CartasBocaAbajo[-1]["palo"] == "espada":
                        print("-----------------------------------")
                        print ("Retrocede el caballo de "+"\033[;34m"+"Espada :c"+"\033[0;m")
                        print("-----------------------------------")
                        ContadorEspada = ContadorEspada - 1
                    if CartasBocaAbajo[-1]["palo"] == "basto":
                        print("-----------------------------------")
                        print ("Retrocede el caballo de "+"\033[;32m"+"Basto :c"+"\033[0;m")
                        print("-----------------------------------")
                        ContadorBasto = ContadorBasto - 1
                    if CartasBocaAbajo[-1]["palo"] == "oro":
                        print("-----------------------------------")
                        print ("Retrocede el caballo de "+"\033[;33m"+"Oro :c"+"\033[0;m")
                        print("-----------------------------------")
                        ContadorOro = ContadorOro - 1
                    if CartasBocaAbajo[-1]["palo"] == "copa":
                        print("-----------------------------------")
                        print ("Retrocede el caballo de "+"\033[;31m"+"Copas :c"+"\033[0;m")
                        print("-----------------------------------")
                        ContadorCopa = ContadorCopa - 1

                    CartasBocaAbajo.pop(-1)

            caballos(ContadorBasto,ContadorCopa,ContadorOro,ContadorEspada,EvPos)
            
            if (ContadorEspada > 11) or (ContadorOro > 11 )or(ContadorBasto > 11) or (ContadorCopa > 11):
                print("----------------------------")
                print("Tenemos un ganador!!!!!!")
                print("El ganador es......")
                print("----------------------------")
                if (ContadorEspada > ContadorOro) and (ContadorEspada > ContadorBasto) and (ContadorEspada > ContadorCopa):
                    print("\033[;34m"+"----------------------------"+"\033[0;m")
                    print("El caballo de "+"\033[;34m"+"Espada!!!"+"\033[0;m")
                    print("\033[;34m"+"----------------------------"+"\033[0;m")
                elif (ContadorBasto > ContadorOro) and (ContadorBasto > ContadorEspada) and (ContadorBasto > ContadorCopa):
                    print("\033[;32m"+"----------------------------"+"\033[0;m")
                    print("El caballo de "+"\033[;32m"+"Basto!!!"+"\033[0;m")
                    print("\033[;32m"+"----------------------------"+"\033[0;m")
                elif (ContadorOro > ContadorEspada) and (ContadorOro > ContadorBasto) and (ContadorOro > ContadorCopa):
                    print("\033[;33m"+"----------------------------"+"\033[0;m")
                    print("El caballo de "+"\033[;33m"+"Oro!!!"+"\033[0;m")
                    print("\033[;33m"+"----------------------------"+"\033[0;m")
                elif (ContadorCopa > ContadorOro) and (ContadorCopa > ContadorBasto) and (ContadorCopa > ContadorEspada):
                    print("\033[;31m"+"----------------------------"+"\033[0;m")
                    print("El caballo de "+"\033[;31m"+"Copas!!!"+"\033[0;m")
                    print("\033[;31m"+"----------------------------"+"\033[0;m")
                #Finalizacion del juego    
                input()
                system("cls")
                break
            
            
            #Printeo de puntajes
            print("\033[;34m"+"Espada:"+"\033[0;m", ContadorEspada)
            print("\033[;32m"+"Basto:"+"\033[0;m", ContadorBasto)
            print("\033[;33m"+"Oro:"+"\033[0;m", ContadorOro)
            print("\033[;31m"+"Copa:"+"\033[0;m", ContadorCopa)
            input()
            system("cls")
            
                

    elif respuesta == 2:
        exit()

