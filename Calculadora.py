import os
import time
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(("------ Bienvenido ------\n").center(50," "))
    def octal(x):
        return oct(x)
    def hexadecimal(x):
        return hex(x)
    def binario(x):
        return bin(x)
    n1 = int(input("Escriba su primer número en decimal: "))
    n2 = int(input("Escriba su segundo número en decimal: "))
    x = str(input("\nSi desea ver su numero en octal escribir (o), hexadecimal (h) y Binario (b): "))
    if x == "o":
        print("Sus numeros en octal son: ", octal(n1), "-", octal(n2))
        a = n1 * n2
        print("El resultado de la multiplicación de los dos numeros es: ", octal(a))
    if x == "h":
        print("Sus numeros en Hexadecimal son: ", hexadecimal(n1), "-", hexadecimal(n2))
        a = n1 * n2
        print("El resultado de la multiplicación de los dos numeros es: ", hexadecimal(a))
    if x == "b":
        print("Sus numeros en binario son: ", binario(n1), "-", binario(n2))
        a = n1 * n2
        print("El resultado de la multiplicación de los dos numeros es: ", binario(a))
    print("****Dar enter para continuar****".center(50," "))
    input("")