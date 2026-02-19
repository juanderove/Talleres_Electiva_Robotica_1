"""3. Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro)
donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen."""
import math

print("1  Prisma")
print("2  Pirámide")
print("3  Cono truncado")
print("4  Cilindo")
opcion = int(input("Ingrese el el cuerpo geometrico al cual desea calcular su volumen: "))


def prisma():
    print("\nVolumen de un Prisma:")
    largo = float(input("Ingrese el largo de la base: "))
    ancho = float(input("Ingrese el ancho de la base: "))
    altura = float(input("Ingrese la altura: "))
    
    # Volumen del Prisma:
    volumen = largo * ancho * altura
    
    print(f"El volumen del Prisma es: {volumen}")

def piramide():
    print("\nVolumen de una piramide:")
    largo = float(input("Ingrese el largo de la base: "))
    ancho = float(input("Ingrese el ancho de la base: "))
    altura = float(input("Ingrese la altura: "))
    
    # Volumen de la Piramide:
    volumen = (largo * ancho * altura)/3
    
    print(f"El volumen de la Piramide es: {volumen}")

def conoTruncado():
    print("\nVolumen de un Cono Truncado:")
    R = float(input("Ingrese el radio mayor: "))
    r = float(input("Ingrese el radio menor: "))
    h = float(input("Ingrese la altura: "))
    
    # Volumen de un Cono Truncado:
    volumen = (math.pi * h * (R**2 + r**2 + R * r))/3
    
    print(f"El volumen del Cono Truncado es: {volumen}")
    
def cilindro():
    print("\nVolumen de un Ciindro:")
    r = float(input("Ingrese el radio: "))
    h = float(input("Ingrese la altura: "))
    
    # Volumen de un Cilindro:
    volumen = math.pi * r**2 * h
    
    print(f"El volumen del Cilindro es: {volumen}")
 

# -> Opciones:   
if opcion == 1:
   prisma()
elif opcion == 2:
    piramide()
elif opcion == 3:
    conoTruncado()
elif opcion == 4:
    cilindro()
else:
    print("Opción No Valida")
    
    
    



    
