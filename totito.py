#  1   2   3   4   5 
#A . | . | . | . | .
#  ------------------
#C . | . | . | . | .
#  ------------------
#E . | . | . | . | .
#  ------------------
#G . | . | . | . | .
#  ------------------
#I . | . | . | . | .

import time
import random
import os
#importar librerias
os.system('cls' if os.name == 'nt' else 'clear')
#limpiar pantalla
while True:
    print("********* Bienvenido ***********".center(50," "))
    print("\nSeleccione una de las siguientes opciones:")
    print("1. Comenzar juego")
    print("2. Salir\n")
    opcion = int(input("Ingresar opcion: "))
    if opcion == 1:
        lista_A = [".","|",".","|",".","|",".","|","."]
        lista_B = ["_____|_________|_________|_________|_____"]
        lista_C = [".","|",".","|",".","|",".","|","."]
        lista_D = ["_____|_________|_________|_________|_____"]
        lista_E = [".","|",".","|",".","|",".","|","."]
        lista_F = ["_____|_________|_________|_________|_____"]
        lista_G = [".","|",".","|",".","|",".","|","."]
        lista_H = ["_____|_________|_________|_________|_____"]
        lista_I = [".","|",".","|",".","|",".","|","."]

        Lista_posiones = ["A,1", "A,2", "A,3", "A,4", "A,5", "B,1", "B,2", "B,3","B,4","B,5", "C,1", "C,2", "C,3", "C,4", "C,5", "D,1", "D,2", "D,3", "D,4", "D,5", "E,1", "E,2", "E,3", "E,4", "E,5"]
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("********* Juego Totito ***********".center(50," "))
        print ("""\nEl tablero está conformado por columnas y filas
  1   2   3   4   5
A .   .   .   .   .
B .   .   .   .   .
C .   .   .   .   .
D .   .   .   .   .            
E .   .   .   .   .
Columnas: 1 2 3 4 5 
Filas: A B C D E

Para ingresar la posición que quieres hazlo como un tablero de ajedrez colova primero tu columna y luego tú fila y hazte con la Victoria!
               """)
        print("\n1. Comenzar Jugando")
        print("2. IA comienza\n")
        opcion1 = int(input("Ingresar opcion: "))
        if opcion1 == 1:
            l = 0
            def turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I):
                ia = random.choice(Lista_posiones)
                Lista_posiones.remove(ia)
                if ia == "A,1":
                    lista_A[0] = "O"
                elif ia == "A,2":
                    lista_A[2] = "O"
                elif ia == "A,3":
                    lista_A[4] = "O"
                elif ia == "A,4":
                    lista_A[6] = "O"
                elif ia == "A,5":
                    lista_A[8] = "O"

                elif ia == "B,1":
                    lista_C[0] = "O"
                elif ia == "B,2":
                    lista_C[2] = "O"
                elif ia == "B,3":
                    lista_C[4] = "O"
                elif ia == "B,4":
                    lista_C[6] = "O"
                elif ia == "B,5":
                    lista_C[8] = "O"
                
                elif ia == "C,1":
                    lista_E[0] = "O"
                elif ia == "C,2":
                    lista_E[2] = "O"
                elif ia == "C,3":
                    lista_E[4] = "O"
                elif ia == "C,4":
                    lista_E[6] = "O"
                elif ia == "C,5":
                    lista_E[8] = "O"
                
                elif ia == "D,1":
                    lista_G[0] = "O"
                elif ia == "D,2":
                    lista_G[2] = "O"
                elif ia == "D,3":
                    lista_G[4] = "O"
                elif ia == "D,4":
                    lista_G[6] = "O"
                elif ia == "D,5":
                    lista_G[8] = "O"
                
                elif ia == "E,1":
                    lista_I[0] = "O"
                elif ia == "E,2":
                    lista_I[2] = "O"
                elif ia == "E,3":
                    lista_I[4] = "O"
                elif ia == "E,4":
                    lista_I[6] = "O"
                elif ia == "E,5":
                    lista_I[8] = "O"

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("********* Juego Totito ***********".center(50," "))
                print()
                print(lista_A)
                print(lista_B)
                print(lista_C)
                print(lista_D)
                print(lista_E)
                print(lista_F)
                print(lista_G)
                print(lista_H)
                print(lista_I)
                print()
                print("\nLas posiciones disponibles son:\n")
                print(Lista_posiones)
                lista_letra = ["A", "B", "C", "D", "E"]
                lista_numeros = [1, 2, 3, 4, 5]
                while True:
                    letra = str(input("Ingresar la coordenada en letras: ")) 
                    letra = letra.upper()
                    numero = int(input("Ingresar la coordenada en numeros: "))
                    if letra in lista_letra and numero in lista_numeros:
                        if letra == "A" and numero == 1:
                            if "A,1" in Lista_posiones:
                                lista_A[0] = "X"
                                Lista_posiones.remove("A,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "A" and numero == 2:
                            if "A,2" in Lista_posiones:
                                lista_A[2] = "X"
                                Lista_posiones.remove("A,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                
                        elif letra == "A" and numero == 3:
                            if "A,3" in Lista_posiones:
                                lista_A[4] = "X"
                                Lista_posiones.remove("A,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
        
                        elif letra == "A" and numero == 4: 
                            if "A,4" in Lista_posiones:
                                lista_A[6] = "X"
                                Lista_posiones.remove("A,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "A" and numero == 5:
                            if "A,5" in Lista_posiones:
                                lista_A[8] = "X"
                                Lista_posiones.remove("A,5")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "B" and numero == 1:
                            if "B,1" in Lista_posiones:
                                lista_C[0] = "X"
                                Lista_posiones.remove("B,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "B" and numero == 2:
                            if "B,2" in Lista_posiones:
                                lista_C[2] = "X"
                                Lista_posiones.remove("B,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "B" and numero == 3:
                            if "B,3"in Lista_posiones:
                                lista_C[4] = "X"
                                Lista_posiones.remove("B,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "B" and numero == 4:
                            if "B,4" in Lista_posiones:
                                lista_C[6] = "X"
                                Lista_posiones.remove("B,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "B" and numero == 5:
                            if "B,5" in Lista_posiones:
                                lista_C[8] = "X"
                                Lista_posiones.remove("B,5")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "C" and numero == 1:
                            if "C,1" in Lista_posiones:
                                lista_E[0] = "X"
                                Lista_posiones.remove("C,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "C" and numero == 2:
                            if "C,2" in Lista_posiones:
                                lista_E[2] = "X"
                                Lista_posiones.remove("C,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "C" and numero == 3:
                            if "C,3" in Lista_posiones:
                                lista_E[4] = "X"
                                Lista_posiones.remove("C,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "C" and numero == 4:
                            if "C,4" in Lista_posiones:
                                lista_E[6] = "X"
                                Lista_posiones.remove("C,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "C" and numero == 5:
                            if "C,5" in Lista_posiones:
                                lista_E[8] = "X"
                                Lista_posiones.remove("C,5")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "D" and numero == 1:
                            if "D,1" in Lista_posiones:
                                lista_G[0] = "X"
                                Lista_posiones.remove("D,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "D" and numero == 2:
                            if "D,2" in Lista_posiones:
                                lista_G[2] = "X"
                                Lista_posiones.remove("D,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "D" and numero == 3:
                            if "D,3" in Lista_posiones:
                                lista_G[4] = "X"
                                Lista_posiones.remove("D,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "D" and numero == 4:
                            if "D,4" in Lista_posiones:
                                lista_G[6] = "X"
                                Lista_posiones.remove("D,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "D" and numero == 5:
                            if "D,5" in Lista_posiones:
                                lista_G[8] = "X"
                                Lista_posiones.remove("D,5")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 1:
                            if "E,1" in Lista_posiones:
                                lista_I[0] = "X"
                                Lista_posiones.remove("E,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 2:
                            if "E,2" in Lista_posiones:
                                lista_I[2] = "X"
                                Lista_posiones.remove("E,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 3:
                            if "E,3" in Lista_posiones:
                                lista_I[4] = "X"
                                Lista_posiones.remove("E,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 4:
                            if "E,4" in Lista_posiones:
                                lista_I[6] = "X"
                                Lista_posiones.remove("E,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 5:
                            if "E,5" in Lista_posiones:
                                lista_I[8] = "X"
                                Lista_posiones.remove("E,5")
                                break 
                            else:
                                print("Coordenada ingresada ya ocupada")
                    else:
                        print("Ingresar una coordenada válida")
                    
                print()
                print(lista_A)
                print(lista_B)
                print(lista_C)
                print(lista_D)
                print(lista_E)
                print(lista_F)
                print(lista_G)
                print(lista_H)
                print(lista_I)
                print()
                #verticales
                if lista_A[0] == "X" and lista_C[0] == "X" and lista_E[0] == "X" and lista_G[0] == "X" and lista_I[0] == "X":
                    print("Ha ganado")
                    break
                elif lista_A[2] == "X" and lista_C[2] == "X" and lista_E[2] == "X" and lista_G[2] == "X" and lista_I[2] == "X":
                    print("Ha ganado")
                    break
                elif lista_A[4] == "X" and lista_C[4] == "X" and lista_E[4] == "X" and lista_G[4] == "X" and lista_I[4] == "X":
                    print("Ha ganado")
                    break
                elif lista_A[6] == "X" and lista_C[6] == "X" and lista_E[6] == "X" and lista_G[6] == "X" and lista_I[6] == "X":
                    print("Ha ganado")
                    break
                elif lista_A[8] == "X" and lista_C[8] == "X" and lista_E[8] == "X" and lista_G[8] == "X" and lista_I[8] == "X":
                    print("Ha ganado")
                    break

                #horizonatales
                elif lista_A[0] == "X" and lista_A[2] == "X" and lista_A[4] == "X" and lista_A[6] == "X" and lista_A[8] == "X":
                    print("Ha ganado")
                    break
                elif lista_C[0] == "X" and lista_C[2] == "X" and lista_C[4] == "X" and lista_C[6] == "X" and lista_C[8] == "X":
                    print("Ha ganado")
                    break
                elif lista_E[0] == "X" and lista_E[2] == "X" and lista_E[4] == "X" and lista_E[6] == "X" and lista_E[8] == "X":
                    print("Ha ganado")
                    break
                elif lista_G[0] == "X" and lista_G[2] == "X" and lista_G[4] == "X" and lista_G[6] == "X" and lista_G[8] == "X":
                    print("Ha ganado")
                    break
                elif lista_I[0] == "X" and lista_I[2] == "X" and lista_I[4] == "X" and lista_I[6] == "X" and lista_I[8] == "X":
                    print("Ha ganado")
                    break

                #Diagonales

                elif lista_A[0] == "X" and lista_C[2] == "X" and lista_E[4] == "X" and lista_G[6] == "X" and lista_I[8] == "X":
                    print("Ha ganado")
                    break
                elif lista_A[8] == "X" and lista_C[6] == "X" and lista_E[4] == "X" and lista_G[2] == "X" and lista_I[0] == "X":
                    print("Ha ganado")
                    break
                l = l+1
                if l == 25:
                    print("Empate!")
                    break
                print()
                print("LA IA ESTA ELIGIENDO...")
                print()
                time.sleep(3)
                if lista_E[4]== ".":
                    lista_E[4] = "O"
                    Lista_posiones.remove("C,3")
                elif lista_A[0] == "X" and lista_C[0] == "X" and lista_E[0] == "X" and lista_G[0] == "X":
                    if "E,1" in Lista_posiones:
                        lista_I[0] = "O"
                        Lista_posiones.remove("E,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_C[0] == "X" and lista_E[0] == "X" and lista_I[0] == "X":
                    if "D,1" in Lista_posiones:
                        lista_G[0] = "O"
                        Lista_posiones.remove("D,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
  
                elif lista_A[0] == "X" and lista_C[0] == "X" and lista_I[0] == "X" and lista_G[0] == "X":
                    if "C,1" in Lista_posiones:
                        lista_E[0] = "O"
                        Lista_posiones.remove("C,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_I[0] == "X" and lista_E[0] == "X" and lista_G[0] == "X":
                    if "B,1" in Lista_posiones:
                        lista_C[0] = "O"
                        Lista_posiones.remove("B,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "X" and lista_C[0] == "X" and lista_E[0] == "X" and lista_G[0] == "X":
                    if "A,1" in Lista_posiones:
                        lista_A[0] = "O"
                        Lista_posiones.remove("A,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                        
                elif lista_A[2] == "X" and lista_C[2] == "X" and lista_E[2] == "X" and lista_G[2] == "X":
                    if "E,2" in Lista_posiones:
                        lista_I[2] = "O"
                        Lista_posiones.remove("E,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[2] == "X" and lista_C[2] == "X" and lista_E[2] == "X" and lista_I[2] == "X":
                    if "D,2" in Lista_posiones:
                        lista_G[2] = "O"
                        Lista_posiones.remove("D,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                
                elif lista_A[2] == "X" and lista_C[2] == "X" and lista_I[2] == "X" and lista_G[2] == "X":
                    if "C,2" in Lista_posiones:
                        lista_E[2] = "O"
                        Lista_posiones.remove("C,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[2] == "X" and lista_I[2] == "X" and lista_E[2] == "X" and lista_G[2] == "X":
                    if "B,2" in Lista_posiones:
                        lista_C[2] = "O"
                        Lista_posiones.remove("B,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[2] == "X" and lista_C[2] == "X" and lista_E[2] == "X" and lista_G[2] == "X":
                    if "A,2" in Lista_posiones:
                        lista_A[2] = "O"
                        Lista_posiones.remove("A,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[4] == "X" and lista_C[4] == "X" and lista_E[4] == "X" and lista_G[4] == "X":
                    if "E,3" in Lista_posiones:
                        lista_I[4] = "O"
                        Lista_posiones.remove("E,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[4] == "X" and lista_C[4] == "X" and lista_E[4] == "X" and lista_I[4] == "X":
                    if "D,3" in Lista_posiones:
                        lista_G[4] = "O"
                        Lista_posiones.remove("D,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[4] == "X" and lista_C[4] == "X" and lista_I[4] == "X" and lista_G[4] == "X":
                    if "C,3" in Lista_posiones:
                        lista_E[4] = "O"
                        Lista_posiones.remove("C,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[4] == "X" and lista_I[4] == "X" and lista_E[4] == "X" and lista_G[4] == "X":
                    if "B,3" in Lista_posiones:
                        lista_C[4] = "O"
                        Lista_posiones.remove("B,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[4] == "X" and lista_C[4] == "X" and lista_E[4] == "X" and lista_G[4] == "X":
                    if "A,3" in Lista_posiones:
                        lista_A[4] = "O"
                        Lista_posiones.remove("A,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[6] == "X" and lista_C[6] == "X" and lista_E[6] == "X" and lista_G[6] == "X":
                    if "E,4" in Lista_posiones:
                        lista_I[6] = "O"
                        Lista_posiones.remove("E,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[6] == "X" and lista_C[6] == "X" and lista_E[6] == "X" and lista_I[6] == "X":
                    if "D,4" in Lista_posiones:
                        lista_G[6] = "O"
                        Lista_posiones.remove("D,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[6] == "X" and lista_C[6] == "X" and lista_I[6] == "X" and lista_G[6] == "X":
                    if "C,4" in Lista_posiones:
                        lista_E[6] = "O"
                        Lista_posiones.remove("C,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[6] == "X" and lista_I[6] == "X" and lista_E[6] == "X" and lista_G[6] == "X":
                    if "B,4" in Lista_posiones:
                        lista_C[6] = "O"
                        Lista_posiones.remove("B,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[6] == "X" and lista_C[6] == "X" and lista_E[6] == "X" and lista_G[6] == "X":
                    if "A,4" in Lista_posiones:
                        lista_A[6] = "O"
                        Lista_posiones.remove("A,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "X" and lista_C[8] == "X" and lista_E[8] == "X" and lista_G[8] == "X":
                    if "E,5" in Lista_posiones:
                        lista_I[8] = "O"
                        Lista_posiones.remove("E,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "X" and lista_C[8] == "X" and lista_E[8] == "X" and lista_I[8] == "X":
                    if "D,5" in Lista_posiones:
                        lista_G[8] = "O"
                        Lista_posiones.remove("D,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "X" and lista_C[8] == "X" and lista_I[8] == "X" and lista_G[8] == "X":
                    if "C,5" in Lista_posiones:
                        lista_E[8] = "O"
                        Lista_posiones.remove("C,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "X" and lista_I[8] == "X" and lista_E[8] == "X" and lista_G[8] == "X":
                    if "B,5" in Lista_posiones:
                        lista_C[8] = "O"
                        Lista_posiones.remove("B,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                       
                elif lista_I[8] == "X" and lista_C[8] == "X" and lista_E[8] == "X" and lista_G[8] == "X":
                    if "A,5" in Lista_posiones:
                        lista_A[8] = "O"
                        Lista_posiones.remove("A,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_A[2] == "X" and lista_A[4] == "X" and lista_A[6] == "X":
                    if "A,5" in Lista_posiones:
                        lista_A[8] = "O"
                        Lista_posiones.remove("A,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_A[2] == "X" and lista_A[4] == "X" and lista_A[8] == "X":
                    if "A,4" in Lista_posiones:
                        lista_A[6] = "O"
                        Lista_posiones.remove("A,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_A[2] == "X" and lista_A[8] == "X" and lista_A[6] == "X":
                    if "A,3" in Lista_posiones:
                        lista_A[4] = "O"
                        Lista_posiones.remove("A,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_A[4] == "X" and lista_A[8] == "X" and lista_A[6] == "X":
                    if "A,2" in Lista_posiones:
                        lista_A[2] = "O"
                        Lista_posiones.remove("A,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[4] == "X" and lista_A[2] == "X" and lista_A[8] == "X" and lista_A[6] == "X":
                    if "A,1" in Lista_posiones:
                        lista_A[0] = "O"
                        Lista_posiones.remove("A,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[0] == "X" and lista_C[2] == "X" and lista_C[4] == "X" and lista_C[6] == "X":
                    if "B,5" in Lista_posiones:
                        lista_C[8] = "O"
                        Lista_posiones.remove("B,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[0] == "X" and lista_C[2] == "X" and lista_C[4] == "X" and lista_C[8] == "X":
                    if "B,4" in Lista_posiones:
                        lista_C[6] = "O"
                        Lista_posiones.remove("B,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[0] == "X" and lista_C[2] == "X" and lista_C[8] == "X" and lista_C[6] == "X":
                    if "B,3" in Lista_posiones:
                        lista_C[4] = "O"
                        Lista_posiones.remove("B,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[0] == "X" and lista_C[8] == "X" and lista_C[4] == "X" and lista_C[6] == "X":
                    if "B,2" in Lista_posiones:
                        lista_C[2] = "O"
                        Lista_posiones.remove("B,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[8] == "X" and lista_C[2] == "X" and lista_C[4] == "X" and lista_C[6] == "X":
                    if "B,1" in Lista_posiones:
                        lista_C[0] = "O"
                        Lista_posiones.remove("B,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_E[0] == "X" and lista_E[2] == "X" and lista_E[4] == "X" and lista_E[6] == "X":
                    if "C,5" in Lista_posiones:
                        lista_E[8] = "O"
                        Lista_posiones.remove("C,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                        
                elif lista_E[0] == "X" and lista_E[2] == "X" and lista_E[4] == "X" and lista_E[8] == "X":
                    if "C,4" in Lista_posiones:
                        lista_E[6] = "O"
                        Lista_posiones.remove("C,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_E[0] == "X" and lista_E[2] == "X" and lista_E[8] == "X" and lista_E[6] == "X":
                    if "C,3" in Lista_posiones:
                        lista_E[4] = "O"
                        Lista_posiones.remove("C,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_E[0] == "X" and lista_E[8] == "X" and lista_E[4] == "X" and lista_E[6] == "X":
                    if "C,2" in Lista_posiones:
                        lista_E[2] = "O"
                        Lista_posiones.remove("C,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_E[8] == "X" and lista_E[2] == "X" and lista_E[4] == "X" and lista_E[6] == "X":
                    if "C,1" in Lista_posiones:
                        lista_E[0] = "O"
                        Lista_posiones.remove("C,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[0] == "X" and lista_G[2] == "X" and lista_G[4] == "X" and lista_G[6] == "X":
                    if "D,5" in Lista_posiones:
                        lista_G[8] = "O"
                        Lista_posiones.remove("D,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[0] == "X" and lista_G[2] == "X" and lista_G[4] == "X" and lista_G[8] == "X":
                    if "D,4" in Lista_posiones:
                        lista_G[6] = "O"
                        Lista_posiones.remove("D,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[0] == "X" and lista_G[2] == "X" and lista_G[8] == "X" and lista_G[6] == "X":
                    if "D,3" in Lista_posiones:
                        lista_G[4] = "O"
                        Lista_posiones.remove("D,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[0] == "X" and lista_G[8] == "X" and lista_G[4] == "X" and lista_G[6] == "X":
                    if "D,2" in Lista_posiones:
                        lista_G[2] = "O"
                        Lista_posiones.remove("D,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[8] == "X" and lista_G[2] == "X" and lista_G[4] == "X" and lista_G[6] == "X":
                    if "D,1" in Lista_posiones:
                        lista_G[0] = "O"
                        Lista_posiones.remove("D,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "X" and lista_I[2] == "X" and lista_I[4] == "X" and lista_I[6] == "X":
                    if "E,5" in Lista_posiones:
                        lista_I[8] = "O"
                        Lista_posiones.remove("E,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "X" and lista_I[2] == "X" and lista_I[4] == "X" and lista_I[8] == "X":
                    if "E,4" in Lista_posiones:
                        lista_I[6] = "O"
                        Lista_posiones.remove("E,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "X" and lista_I[2] == "X" and lista_I[8] == "X" and lista_I[6] == "X":
                    if "E,3" in Lista_posiones:
                        lista_I[4] = "O"
                        Lista_posiones.remove("E,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "X" and lista_I[8] == "X" and lista_I[4] == "X" and lista_I[6] == "X":
                    if "E,2" in Lista_posiones:
                        lista_I[2] = "O"
                        Lista_posiones.remove("E,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                        
                elif lista_I[8] == "X" and lista_I[2] == "X" and lista_I[4] == "X" and lista_I[6] == "X":
                    if "E,1" in Lista_posiones:
                        lista_I[0] = "O"
                        Lista_posiones.remove("E,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_C[2] == "X" and lista_E[4] == "X" and lista_G[6] == "X":
                    if "E,5" in Lista_posiones:
                        lista_I[8] = "O"
                        Lista_posiones.remove("E,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_C[2] == "X" and lista_E[4] == "X" and lista_I[8] == "X":
                    if "D,4" in Lista_posiones:
                        lista_G[6] = "O"
                        Lista_posiones.remove("D,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_C[2] == "X" and lista_I[8] == "X" and lista_G[6] == "X":
                    if "C,3" in Lista_posiones:
                        lista_E[4] = "O"
                        Lista_posiones.remove("C,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "X" and lista_I[8] == "X" and lista_E[4] == "X" and lista_G[6] == "X":
                    if "B,2" in Lista_posiones:
                        lista_C[2] = "O"
                        Lista_posiones.remove("B,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[8] == "X" and lista_C[2] == "X" and lista_E[4] == "X" and lista_G[6] == "X":
                    if "A,1" in Lista_posiones:
                        lista_A[0] = "O"
                        Lista_posiones.remove("A,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "X" and lista_C[6] == "X" and lista_E[4] == "X" and lista_G[2] == "X":
                    if "E,1" in Lista_posiones:
                        lista_I[0] = "O"
                        Lista_posiones.remove("E,1")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "X" and lista_C[6] == "X" and lista_E[4] == "X" and lista_I[0] == "X":
                    if "D,2" in Lista_posiones:
                        lista_G[2] = "O"
                        Lista_posiones.remove("D,2")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "X" and lista_C[6] == "X" and lista_I[0] == "X" and lista_G[2] == "X":
                    if "C,3" in Lista_posiones:
                        lista_E[4] = "O"
                        Lista_posiones.remove("C,3")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "X" and lista_I[0] == "X" and lista_E[4] == "X" and lista_G[2] == "X":
                    if "B,4" in Lista_posiones:
                        lista_C[6] = "O"
                        Lista_posiones.remove("B,4")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "X" and lista_C[6] == "X" and lista_E[4] == "X" and lista_G[2] == "X":
                    if "A,5" in Lista_posiones:
                        lista_A[8] = "O"
                        Lista_posiones.remove("A,5")
                    else:
                        turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                else:
                    turno_IA(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                print()
                print(lista_A)
                print(lista_B)
                print(lista_C)
                print(lista_D)
                print(lista_E)
                print(lista_F)
                print(lista_G)
                print(lista_H)
                print(lista_I)
                print()
                #verticales
                if lista_A[0] == "O" and lista_C[0] == "O" and lista_E[0] == "O" and lista_G[0] == "O" and lista_I[0] == "O":
                    print("la maquina ha ganado")
                    break
                elif lista_A[2] == "O" and lista_C[2] == "O" and lista_E[2] == "O" and lista_G[2] == "O" and lista_I[2] == "O":
                    print("la maquina ha ganado")
                    break
                elif lista_A[4] == "O" and lista_C[4] == "O" and lista_E[4] == "O" and lista_G[4] == "O" and lista_I[4] == "O":
                    print("la maquina ha ganado")
                    break
                elif lista_A[6] == "O" and lista_C[6] == "O" and lista_E[6] == "O" and lista_G[6] == "O" and lista_I[6] == "O":
                    print("la maquina ha ganado")
                    break
                elif lista_A[8] == "O" and lista_C[8] == "O" and lista_E[8] == "O" and lista_G[8] == "O" and lista_I[8] == "O":
                    print("la maquina ha ganado")
                    break

                #horizonatales
                elif lista_A[0] == "O" and lista_A[2] == "O" and lista_A[4] == "O" and lista_A[6] == "O" and lista_A[8] == "O":
                    print("la maquina ha ganado")
                    break
                elif lista_C[0] == "O" and lista_C[2] == "O" and lista_C[4] == "O" and lista_C[6] == "O" and lista_C[8] == "O":
                    print("la maquina ha ganado")
                    break
                elif lista_E[0] == "O" and lista_E[2] == "O" and lista_E[4] == "O" and lista_E[6] == "O" and lista_E[8] == "O":
                    print("la maquina ha ganado")
                    break
                elif lista_G[0] == "O" and lista_G[2] == "O" and lista_G[4] == "O" and lista_G[6] == "O" and lista_G[8] == "O":
                    print("la maquina ha ganado")
                    break
                elif lista_I[0] == "O" and lista_I[2] == "O" and lista_I[4] == "O" and lista_I[6] == "O" and lista_I[8] == "O":
                    print("la maquina ha ganado")
                    break

                #Diagonales

                elif lista_A[0] == "O" and lista_C[2] == "O" and lista_E[4] == "O" and lista_G[6] == "O" and lista_I[8] == "O":
                    print("la maquina ha ganado")
                    break
                elif lista_A[8] == "O" and lista_C[6] == "O" and lista_E[4] == "O" and lista_G[2] == "O" and lista_I[0] == "O":
                    print("la maquina ha ganado")
                    break
                l = l+1
                if l == 25:
                    print("Empate!")
                    break
        if opcion1 == 2:
            l = 0
            def turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I):
                ia = random.choice(Lista_posiones)
                Lista_posiones.remove(ia)
                if ia == "A,1":
                    lista_A[0] = "X"
                elif ia == "A,2":
                    lista_A[2] = "X"
                elif ia == "A,3":
                    lista_A[4] = "X"
                elif ia == "A,4":
                    lista_A[6] = "X"
                elif ia == "A,5":
                    lista_A[8] = "X"

                elif ia == "B,1":
                    lista_C[0] = "X"
                elif ia == "B,2":
                    lista_C[2] = "X"
                elif ia == "B,3":
                    lista_C[4] = "X"
                elif ia == "B,4":
                    lista_C[6] = "X"
                elif ia == "B,5":
                    lista_C[8] = "X"
                
                elif ia == "C,1":
                    lista_E[0] = "X"
                elif ia == "C,2":
                    lista_E[2] = "X"
                elif ia == "C,3":
                    lista_E[4] = "X"
                elif ia == "C,4":
                    lista_E[6] = "X"
                elif ia == "C,5":
                    lista_E[8] = "X"
                
                elif ia == "D,1":
                    lista_G[0] = "X"
                elif ia == "D,2":
                    lista_G[2] = "X"
                elif ia == "D,3":
                    lista_G[4] = "X"
                elif ia == "D,4":
                    lista_G[6] = "X"
                elif ia == "D,5":
                    lista_G[8] = "X"
                
                elif ia == "E,1":
                    lista_I[0] = "X"
                elif ia == "E,2":
                    lista_I[2] = "X"
                elif ia == "E,3":
                    lista_I[4] = "X"
                elif ia == "E,4":
                    lista_I[6] = "X"
                elif ia == "E,5":
                    lista_I[8] = "X"
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("********* Juego Totito ***********".center(50," "))
                print()
                print("LA IA ESTA ELIGIENDO...")
                print()
                time.sleep(3)
                if lista_E[4]== ".":
                    lista_E[4] = "X"
                    Lista_posiones.remove("C,3")
                elif lista_A[0] == "O" and lista_C[0] == "O" and lista_E[0] == "O" and lista_I[0] == "O":
                    if "D,1" in Lista_posiones:
                        lista_G[0] = "X"
                        Lista_posiones.remove("D,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "O" and lista_C[0] == "O" and lista_I[0] == "O" and lista_G[0] == "O":
                    if "C,1" in Lista_posiones:
                        lista_E[0] = "X"
                        Lista_posiones.remove("C,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "O" and lista_I[0] == "O" and lista_E[0] == "O" and lista_G[0] == "O":
                    if "B,1" in Lista_posiones:
                        lista_C[0] = "X"
                        Lista_posiones.remove("B,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "O" and lista_C[0] == "O" and lista_E[0] == "O" and lista_G[0] == "O":
                    if "A,1" in Lista_posiones:
                        lista_A[0] = "X"
                        Lista_posiones.remove("A,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                elif lista_A[2] == "O" and lista_C[2] == "O" and lista_E[2] == "O" and lista_G[2] == "O":
                    if "E,2" in Lista_posiones:
                        lista_I[2] = "X"
                        Lista_posiones.remove("E,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[2] == "O" and lista_C[2] == "O" and lista_E[2] == "O" and lista_I[2] == "O":
                    if "D,2" in Lista_posiones:
                        lista_G[2] = "X"
                        Lista_posiones.remove("D,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                    
                elif lista_A[2] == "O" and lista_C[2] == "O" and lista_I[2] == "O" and lista_G[2] == "O":
                    if "C,2" in Lista_posiones:
                        lista_E[2] = "X"
                        Lista_posiones.remove("C,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[2] == "O" and lista_I[2] == "O" and lista_E[2] == "O" and lista_G[2] == "O":
                    if "B,2" in Lista_posiones:
                        lista_C[2] = "X"
                        Lista_posiones.remove("B,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[2] == "O" and lista_C[2] == "O" and lista_E[2] == "O" and lista_G[2] == "O":
                    if "A,2" in Lista_posiones:
                        lista_A[2] = "X"
                        Lista_posiones.remove("A,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                elif lista_A[4] == "O" and lista_C[4] == "O" and lista_E[4] == "O" and lista_G[4] == "O":
                    if "E,3" in Lista_posiones:
                        lista_I[4] = "X"
                        Lista_posiones.remove("E,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[4] == "O" and lista_C[4] == "O" and lista_E[4] == "O" and lista_I[4] == "O":
                    if "D,3" in Lista_posiones:
                        lista_G[4] = "X"
                        Lista_posiones.remove("D,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[4] == "O" and lista_C[4] == "O" and lista_I[4] == "O" and lista_G[4] == "O":
                    if "C,3" in Lista_posiones:
                        lista_E[4] = "X"
                        Lista_posiones.remove("C,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[4] == "O" and lista_I[4] == "O" and lista_E[4] == "O" and lista_G[4] == "O":
                    if "B,3" in Lista_posiones:
                        lista_C[4] = "X"
                        Lista_posiones.remove("B,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[4] == "O" and lista_C[4] == "O" and lista_E[4] == "O" and lista_G[4] == "O":
                    if "A,3" in Lista_posiones:
                        lista_A[4] = "X"
                        Lista_posiones.remove("A,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                elif lista_A[6] == "O" and lista_C[6] == "O" and lista_E[6] == "O" and lista_G[6] == "O":
                    if "E,4" in Lista_posiones:
                        lista_I[6] = "X"
                        Lista_posiones.remove("E,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[6] == "O" and lista_C[6] == "O" and lista_E[6] == "O" and lista_I[6] == "O":
                    if "D,4" in Lista_posiones:
                        lista_G[6] = "X"
                        Lista_posiones.remove("D,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[6] == "O" and lista_C[6] == "O" and lista_I[6] == "O" and lista_G[6] == "O":
                    if "C,4" in Lista_posiones:
                        lista_E[6] = "X"
                        Lista_posiones.remove("C,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[6] == "O" and lista_I[6] == "O" and lista_E[6] == "O" and lista_G[6] == "O":
                    if "B,4" in Lista_posiones:
                        lista_C[6] = "X"
                        Lista_posiones.remove("B,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[6] == "O" and lista_C[6] == "O" and lista_E[6] == "O" and lista_G[6] == "O":
                    if "A,4" in Lista_posiones:
                        lista_A[6] = "X"
                        Lista_posiones.remove("A,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                elif lista_A[8] == "O" and lista_C[8] == "O" and lista_E[8] == "O" and lista_G[8] == "O":
                    if "E,5" in Lista_posiones:
                        lista_I[8] = "X"
                        Lista_posiones.remove("E,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "O" and lista_C[8] == "O" and lista_E[8] == "O" and lista_I[8] == "O":
                    if "D,5" in Lista_posiones:
                        lista_G[8] = "X"
                        Lista_posiones.remove("D,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "O" and lista_C[8] == "O" and lista_I[8] == "O" and lista_G[8] == "O":
                    if "C,5" in Lista_posiones:
                        lista_E[8] = "X"
                        Lista_posiones.remove("C,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "O" and lista_I[8] == "O" and lista_E[8] == "O" and lista_G[8] == "O":
                    if "B,5" in Lista_posiones:
                        lista_C[8] = "X"
                        Lista_posiones.remove("B,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[8] == "O" and lista_C[8] == "O" and lista_E[8] == "O" and lista_G[8] == "O":
                    if "A,5" in Lista_posiones:
                        lista_A[8] = "X"
                        Lista_posiones.remove("A,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                elif lista_A[0] == "O" and lista_A[2] == "O" and lista_A[4] == "O" and lista_A[6] == "O":
                    if "A,5" in Lista_posiones:
                        lista_A[8] = "X"
                        Lista_posiones.remove("A,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "O" and lista_A[2] == "O" and lista_A[4] == "O" and lista_A[8] == "O":
                    if "A,4" in Lista_posiones:
                        lista_A[6] = "X"
                        Lista_posiones.remove("A,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "O" and lista_A[2] == "O" and lista_A[8] == "O" and lista_A[6] == "O":
                    if "A,3" in Lista_posiones:
                        lista_A[4] = "X"
                        Lista_posiones.remove("A,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "O" and lista_A[4] == "O" and lista_A[8] == "O" and lista_A[6] == "O":
                    if "A,2" in Lista_posiones:
                        lista_A[2] = "X"
                        Lista_posiones.remove("A,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[4] == "O" and lista_A[2] == "O" and lista_A[8] == "O" and lista_A[6] == "O":
                    if "A,1" in Lista_posiones:
                        lista_A[0] = "X"
                        Lista_posiones.remove("A,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[0] == "O" and lista_C[2] == "O" and lista_C[4] == "O" and lista_C[6] == "O":
                    if "B,5" in Lista_posiones:
                        lista_C[8] = "X"
                        Lista_posiones.remove("B,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[0] == "O" and lista_C[2] == "O" and lista_C[4] == "O" and lista_C[8] == "O":
                    if "B,4" in Lista_posiones:
                        lista_C[6] = "X"
                        Lista_posiones.remove("B,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[0] == "O" and lista_C[2] == "O" and lista_C[8] == "O" and lista_C[6] == "O":
                    if "B,3" in Lista_posiones:
                        lista_C[4] = "X"
                        Lista_posiones.remove("B,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[0] == "O" and lista_C[8] == "O" and lista_C[4] == "O" and lista_C[6] == "O":
                    if "B,2" in Lista_posiones:
                        lista_C[2] = "X"
                        Lista_posiones.remove("B,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_C[8] == "O" and lista_C[2] == "O" and lista_C[4] == "O" and lista_C[6] == "O":
                    if "B,1" in Lista_posiones:
                        lista_C[0] = "X"
                        Lista_posiones.remove("B,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_E[0] == "O" and lista_E[2] == "O" and lista_E[4] == "O" and lista_E[6] == "O":
                    if "C,5" in Lista_posiones:
                        lista_E[8] = "X"
                        Lista_posiones.remove("C,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_E[0] == "O" and lista_E[2] == "O" and lista_E[4] == "O" and lista_E[8] == "O":
                    if "C,4" in Lista_posiones:
                        lista_E[6] = "X"
                        Lista_posiones.remove("C,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_E[0] == "O" and lista_E[2] == "O" and lista_E[8] == "O" and lista_E[6] == "O":
                    if "C,3" in Lista_posiones:
                        lista_E[4] = "X"
                        Lista_posiones.remove("C,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_E[0] == "O" and lista_E[8] == "O" and lista_E[4] == "O" and lista_E[6] == "O":
                    if "C,2" in Lista_posiones:
                        lista_E[2] = "X"
                        Lista_posiones.remove("C,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_E[8] == "O" and lista_E[2] == "O" and lista_E[4] == "O" and lista_E[6] == "O":
                    if "C,1" in Lista_posiones:
                        lista_E[0] = "X"
                        Lista_posiones.remove("C,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[0] == "O" and lista_G[2] == "O" and lista_G[4] == "O" and lista_G[6] == "O":
                    if "D,5" in Lista_posiones:
                        lista_G[8] = "X"
                        Lista_posiones.remove("D,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[0] == "O" and lista_G[2] == "O" and lista_G[4] == "O" and lista_G[8] == "O":
                    if "D,4" in Lista_posiones:
                        lista_G[6] = "X"
                        Lista_posiones.remove("D,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[0] == "O" and lista_G[2] == "O" and lista_G[8] == "O" and lista_G[6] == "O":
                    if "D,3" in Lista_posiones:
                        lista_G[4] = "X"
                        Lista_posiones.remove("D,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[0] == "O" and lista_G[8] == "O" and lista_G[4] == "O" and lista_G[6] == "O":
                    if "D,2" in Lista_posiones:
                        lista_G[2] = "X"
                        Lista_posiones.remove("D,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_G[8] == "O" and lista_G[2] == "O" and lista_G[4] == "O" and lista_G[6] == "O":
                    if "D,1" in Lista_posiones:
                        lista_G[0] = "X"
                        Lista_posiones.remove("D,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "O" and lista_I[2] == "O" and lista_I[4] == "O" and lista_I[6] == "O":
                    if "E,5" in Lista_posiones:
                        lista_I[8] = "X"
                        Lista_posiones.remove("E,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "O" and lista_I[2] == "O" and lista_I[4] == "O" and lista_I[8] == "O":
                    if "E,4" in Lista_posiones:
                        lista_I[6] = "X"
                        Lista_posiones.remove("E,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "O" and lista_I[2] == "O" and lista_I[8] == "O" and lista_I[6] == "O":
                    if "E,3" in Lista_posiones:
                        lista_I[4] = "X"
                        Lista_posiones.remove("E,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "O" and lista_I[8] == "O" and lista_I[4] == "O" and lista_I[6] == "O":
                    if "E,2" in Lista_posiones:
                        lista_I[2] = "X"
                        Lista_posiones.remove("E,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[8] == "O" and lista_I[2] == "O" and lista_I[4] == "O" and lista_I[6] == "O":
                    if "E,1" in Lista_posiones:
                        lista_I[0] = "X"
                        Lista_posiones.remove("E,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "O" and lista_C[2] == "O" and lista_E[4] == "O" and lista_G[6] == "O":
                    if "E,5" in Lista_posiones:
                        lista_I[8] = "X"
                        Lista_posiones.remove("E,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "O" and lista_C[2] == "O" and lista_E[4] == "O" and lista_I[8] == "O":
                    if "D,4" in Lista_posiones:
                        lista_G[6] = "X"
                        Lista_posiones.remove("D,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "O" and lista_C[2] == "O" and lista_I[8] == "O" and lista_G[6] == "O":
                    if "C,3" in Lista_posiones:
                        lista_E[4] = "X"
                        Lista_posiones.remove("C,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[0] == "O" and lista_I[8] == "O" and lista_E[4] == "O" and lista_G[6] == "O":
                    if "B,2" in Lista_posiones:
                        lista_C[2] = "X"
                        Lista_posiones.remove("B,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[8] == "O" and lista_C[2] == "O" and lista_E[4] == "O" and lista_G[6] == "O":
                    if "A,1" in Lista_posiones:
                        lista_A[0] = "X"
                        Lista_posiones.remove("A,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "O" and lista_C[6] == "O" and lista_E[4] == "O" and lista_G[2] == "O":
                    if "E,1" in Lista_posiones:
                        lista_I[0] = "X"
                        Lista_posiones.remove("E,1")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "O" and lista_C[6] == "O" and lista_E[4] == "O" and lista_I[0] == "O":
                    if "D,2" in Lista_posiones:
                        lista_G[2] = "X"
                        Lista_posiones.remove("D,2")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "O" and lista_C[6] == "O" and lista_I[0] == "O" and lista_G[2] == "O":
                    if "C,3" in Lista_posiones:
                        lista_E[4] = "X"
                        Lista_posiones.remove("C,3")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_A[8] == "O" and lista_I[0] == "O" and lista_E[4] == "O" and lista_G[2] == "O":
                    if "B,4" in Lista_posiones:
                        lista_C[6] = "X"
                        Lista_posiones.remove("B,4")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                elif lista_I[0] == "O" and lista_C[6] == "O" and lista_E[4] == "O" and lista_G[2] == "O":
                    if "A,5" in Lista_posiones:
                        lista_A[8] = "X"
                        Lista_posiones.remove("A,5")
                    else:
                        turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)

                else:
                    turno_IA2(Lista_posiones, lista_A, lista_C, lista_E, lista_G, lista_I)
                print()
                print(lista_A)
                print(lista_B)
                print(lista_C)
                print(lista_D)
                print(lista_E)
                print(lista_F)
                print(lista_G)
                print(lista_H)
                print(lista_I)
                print()

                #verticales
                if lista_A[0] == "X" and lista_C[0] == "X" and lista_E[0] == "X" and lista_G[0] == "X" and lista_I[0] == "X":
                    print("la maquina ha ganado")
                    break
                elif lista_A[2] == "X" and lista_C[2] == "X" and lista_E[2] == "X" and lista_G[2] == "X" and lista_I[2] == "X":
                    print("la maquina ha ganado")
                    break
                elif lista_A[4] == "X" and lista_C[4] == "X" and lista_E[4] == "X" and lista_G[4] == "X" and lista_I[4] == "X":
                    print("la maquina ha ganado")
                    break
                elif lista_A[6] == "X" and lista_C[6] == "X" and lista_E[6] == "X" and lista_G[6] == "X" and lista_I[6] == "X":
                    print("la maquina ha ganado")
                    break
                elif lista_A[8] == "X" and lista_C[8] == "X" and lista_E[8] == "X" and lista_G[8] == "X" and lista_I[8] == "X":
                    print("la maquina ha ganado")
                    break

                #horizonatales
                elif lista_A[0] == "X" and lista_A[2] == "X" and lista_A[4] == "X" and lista_A[6] == "X" and lista_A[8] == "X":
                    print("la maquina ha ganado")
                    break
                elif lista_C[0] == "X" and lista_C[2] == "X" and lista_C[4] == "X" and lista_C[6] == "X" and lista_C[8] == "X":
                    print("la maquina ha ganado")
                    break
                elif lista_E[0] == "X" and lista_E[2] == "X" and lista_E[4] == "X" and lista_E[6] == "X" and lista_E[8] == "X":
                    print("la maquina ha ganado")
                    break
                elif lista_G[0] == "X" and lista_G[2] == "X" and lista_G[4] == "X" and lista_G[6] == "X" and lista_G[8] == "X":
                    print("la maquina ha ganado")
                    break
                elif lista_I[0] == "X" and lista_I[2] == "X" and lista_I[4] == "X" and lista_I[6] == "X" and lista_I[8] == "X":
                    print("la maquina ha ganado")
                    break

                #Diagonales

                elif lista_A[0] == "X" and lista_C[2] == "X" and lista_E[4] == "X" and lista_G[6] == "X" and lista_I[8] == "X":
                    print("la maquina ha ganado")
                    break
                elif lista_A[8] == "X" and lista_C[6] == "X" and lista_E[4] == "X" and lista_G[2] == "X" and lista_I[0] == "X":
                    print("la maquina ha ganado")
                    break

                l = l+1
                if l == 25:
                    print("\nEmpate!")
                    break
                print()
                lista_letra = ["A", "B", "C", "D", "E"]
                lista_numeros = [1, 2, 3, 4, 5]
                while True:
                    letra = str(input("Ingresar la coordenada en letras: ")) 
                    letra = letra.upper()
                    numero = int(input("Ingresar la coordenada en numeros: "))
                    if letra in lista_letra and numero in lista_numeros:
                        if letra == "A" and numero == 1:
                            if "A,1" in Lista_posiones:
                                lista_A[0] = "O"
                                Lista_posiones.remove("A,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "A" and numero == 2:
                            if "A,2" in Lista_posiones:
                                lista_A[2] = "O"
                                Lista_posiones.remove("A,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "A" and numero == 3:
                            if "A,3" in Lista_posiones:
                                lista_A[4] = "O"
                                Lista_posiones.remove("A,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "A" and numero == 4: 
                            if "A,4" in Lista_posiones:
                                lista_A[6] = "O"
                                Lista_posiones.remove("A,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "A" and numero == 5:
                            if "A,5" in Lista_posiones:
                                lista_A[8] = "O"
                                Lista_posiones.remove("A,5")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "B" and numero == 1:
                            if "B,1" in Lista_posiones:
                                lista_C[0] = "O"
                                Lista_posiones.remove("B,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "B" and numero == 2:
                            if "B,2" in Lista_posiones:
                                lista_C[2] = "O"
                                Lista_posiones.remove("B,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "B" and numero == 3:
                            if "B,3"in Lista_posiones:
                                lista_C[4] = "O"
                                Lista_posiones.remove("B,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "B" and numero == 4:
                            if "B,4" in Lista_posiones:
                                lista_C[6] = "O"
                                Lista_posiones.remove("B,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "B" and numero == 5:
                            if "B,5" in Lista_posiones:
                                lista_C[8] = "O"
                                Lista_posiones.remove("B,5")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "C" and numero == 1:
                            if "C,1" in Lista_posiones:
                                lista_E[0] = "O"
                                Lista_posiones.remove("C,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "C" and numero == 2:
                            if "C,2" in Lista_posiones:
                                lista_E[2] = "O"
                                Lista_posiones.remove("C,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "C" and numero == 3:
                            if "C,3" in Lista_posiones:
                                lista_E[4] = "O"
                                Lista_posiones.remove("C,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "C" and numero == 4:
                            if "C,4" in Lista_posiones:
                                lista_E[6] = "O"
                                Lista_posiones.remove("C,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "C" and numero == 5:
                            if "C,5" in Lista_posiones:
                                lista_E[8] = "O"
                                Lista_posiones.remove("C,5")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")

                        elif letra == "D" and numero == 1:
                            if "D,1" in Lista_posiones:
                                lista_G[0] = "O"
                                Lista_posiones.remove("D,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "D" and numero == 2:
                            if "D,2" in Lista_posiones:
                                lista_G[2] = "O"
                                Lista_posiones.remove("D,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "D" and numero == 3:
                            if "D,3" in Lista_posiones:
                                lista_G[4] = "O"
                                Lista_posiones.remove("D,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "D" and numero == 4:
                            if "D,4" in Lista_posiones:
                                lista_G[6] = "O"
                                Lista_posiones.remove("D,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "D" and numero == 5:
                            if "D,5" in Lista_posiones:
                                lista_G[8] = "O"
                                Lista_posiones.remove("D,5")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 1:
                            if "E,1" in Lista_posiones:
                                lista_I[0] = "O"
                                Lista_posiones.remove("E,1")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 2:
                            if "E,2" in Lista_posiones:
                                lista_I[2] = "O"
                                Lista_posiones.remove("E,2")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 3:
                            if "E,3" in Lista_posiones:
                                lista_I[4] = "O"
                                Lista_posiones.remove("E,3")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 4:
                            if "E,4" in Lista_posiones:
                                lista_I[6] = "O"
                                Lista_posiones.remove("E,4")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                        elif letra == "E" and numero == 5:
                            if "E,5" in Lista_posiones:
                                lista_I[8] = "O"
                                Lista_posiones.remove("E,5")
                                break
                            else:
                                print("Coordenada ingresada ya ocupada")
                    else:
                        print("Ingresar una coordenada válida")
                
                print()
                print(lista_A)
                print(lista_B)
                print(lista_C)
                print(lista_D)
                print(lista_E)
                print(lista_F)
                print(lista_G)
                print(lista_H)
                print(lista_I)
                print()
                time.sleep(2)
                #verticales
                if lista_A[0] == "O" and lista_C[0] == "O" and lista_E[0] == "O" and lista_G[0] == "O" and lista_I[0] == "O":
                    print("Ha ganado")
                    break
                elif lista_A[2] == "O" and lista_C[2] == "O" and lista_E[2] == "O" and lista_G[2] == "O" and lista_I[2] == "O":
                    print("Ha ganado")
                    break
                elif lista_A[4] == "O" and lista_C[4] == "O" and lista_E[4] == "O" and lista_G[4] == "O" and lista_I[4] == "O":
                    print("Ha ganado")
                    break
                elif lista_A[6] == "O" and lista_C[6] == "O" and lista_E[6] == "O" and lista_G[6] == "O" and lista_I[6] == "O":
                    print("Ha ganado")
                    break
                elif lista_A[8] == "O" and lista_C[8] == "O" and lista_E[8] == "O" and lista_G[8] == "O" and lista_I[8] == "O":
                    print("Ha ganado")
                    break

                #horizonatales
                elif lista_A[0] == "O" and lista_A[2] == "O" and lista_A[4] == "O" and lista_A[6] == "O" and lista_A[8] == "O":
                    print("Ha ganado")
                    break
                elif lista_C[0] == "O" and lista_C[2] == "O" and lista_C[4] == "O" and lista_C[6] == "O" and lista_C[8] == "O":
                    print("Ha ganado")
                    break
                elif lista_E[0] == "O" and lista_E[2] == "O" and lista_E[4] == "O" and lista_E[6] == "O" and lista_E[8] == "O":
                    print("Ha ganado")
                    break
                elif lista_G[0] == "O" and lista_G[2] == "O" and lista_G[4] == "O" and lista_G[6] == "O" and lista_G[8] == "O":
                    print("Ha ganado")
                    break
                elif lista_I[0] == "O" and lista_I[2] == "O" and lista_I[4] == "O" and lista_I[6] == "O" and lista_I[8] == "O":
                    print("Ha ganado")
                    break

                #Diagonales

                elif lista_A[0] == "O" and lista_C[2] == "O" and lista_E[4] == "O" and lista_G[6] == "O" and lista_I[8] == "O":
                    print("Ha ganado")
                    break
                elif lista_A[8] == "O" and lista_C[6] == "O" and lista_E[4] == "O" and lista_G[2] == "O" and lista_I[0] == "O":
                    print("Ha ganado")
                    break

                l = l+1
                if l == 25:
                    print("Empate!")
                    break
    if opcion == 2:
        print("Gracias por utilizar")
        break