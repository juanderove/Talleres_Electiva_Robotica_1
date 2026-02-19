"""6. Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble
efecto. Debe establecer previamente los valores de presión, así como las dimensiones físicas del
cilindro para realizar el cálculo."""

import math

# -> Funciones:
def calculoAreas(diametro, vastago):
    area_avance = math.pi * (diametro**2) / 4
    area_retroceso = math.pi * (diametro**2 - vastago**2) / 4
    return area_avance, area_retroceso


def calculoFuerzas(presion, area):
    fuerza = presion * area
    return fuerza

    
# -> Datos del Cilindro doble efecto:
presion_bar = 6 # Presion en bares
diametro_mm = 50 # Diametro del piston en mm
vastago_mm = 20 # Diametro del vastago en mm

print("Datos del Cilindo Doble Efecto:")
print(f"Presion del cilindo: {presion_bar} bar")
print(f"Diametro del cilindro: {diametro_mm} mm")
print(f"Diametro del Vastago del Cilindro: {vastago_mm} mm\n")

presion_pa = presion_bar * 100000 # bar a Pascales
diametro_m = diametro_mm / 1000 # mm a metros
vastago_m = vastago_mm / 1000 # mm a metros
    
area_avance, area_retroceso = calculoAreas(diametro_m, vastago_m)

fuerzaAvance = calculoFuerzas(presion_pa, area_avance)
fuerzaRetroceso = calculoFuerzas(presion_pa, area_retroceso)

print(f"La Fuerza de Avance del Cilindro es: {fuerzaAvance} N")
print(f"La Fuerza de Retroceso del Cilindro es: {fuerzaRetroceso} N")


    
