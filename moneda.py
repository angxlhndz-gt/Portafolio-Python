import os
import random
listamoneda1 = ["Cara", "Escudo"]
listamoneda2 = ["Cara", "Escudo"]
if os.path.exists("Tiros.est"):
    os.remove("Tiros.est")
while True:
    print("\n\n\n********* Bienvenido ***********\n".center(50," "))
    print("Seleccione una de las siguientes opciones:")
    print("1. Comenzar juego")
    print("2. Salir\n")
    opcion = int(input("ingresar opcion:"))
    if opcion == 2:
        print("Gracias por utilizar")
        break
    if opcion == 1:
        moneda1cara = 0
        moneda1escudo = 0
        for y in range(0,100):
            z = random.choice(listamoneda1)
            if z == "Cara":
                moneda1cara += 1
                archivo = open("Tiros.est", "a")
                archivo.write(z+"\n")
                archivo.close()

            else:
                moneda1escudo += 1
                archivo = open("Tiros.est", "a")
                archivo.write(z+"\n")
                archivo.close()
        monedacara2 = 0
        monedaescudo2 = 0

        for y in range(0,100):
            z = random.choice(listamoneda2)
            if z == "Cara":
                monedacara2 += 1
                archivo = open("Tiros.est", "a")
                archivo.write(z+"\n")
                archivo.close()

            else:
                monedaescudo2 += 1
                archivo = open("Tiros.est", "a")
                archivo.write(z+"\n")
                archivo.close()
                    

    print("La cantidad de veces que salio cara en la moneda 1 fue: ",moneda1cara)
    print("La cantidad de veces que salio escudo en la moneda 1 fue: ",moneda1escudo)
    print("La cantidad de veces que salio cara en la moneda 2 fue: ",monedacara2)
    print("La cantidad de veces que salio escudo en la moneda 2 fue: ",monedaescudo2)
                
