"""2. Realice un programa que calcule X números aleatorios en un rango determinado por el usuario."""

import random 

cantidad = int(input("Ingese la cantidad de numeros aleatorios que desea generar: "))
inicio = int(input("Ingrese el valor inicial del rango: "))
fin = int(input("Ingrese el valor final del rango: "))

numeros_aleatorios = []
for i in range(cantidad):
    numero = random.randint(inicio, fin)
    numeros_aleatorios.append(numero)

print(f"\nSe generaron {cantidad} valores, en un rango desde {inicio} a {fin}")
print("Los Numeros Aleatorios generados son: ", numeros_aleatorios)