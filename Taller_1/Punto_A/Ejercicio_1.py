"""1. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) 
y divida dos vectores previamente inicializados."""

# Cargamos la libreria para operaciones:
import numpy as np

# Vectores a trabajar:
v1 = np.array([10,20,30])
v2 = np.array([4,5,6])

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")

# OPERACIONES:
# -> Suma:
suma = v1 + v2
print(f"\nSuma de Vectores: {suma}")

# -> Resta:
resta = v1 - v2
print(f"Resta de Vectores: {resta}")

# -> Producto Punto (Escalar):
# prod_punto = np.dot(v1, v2) # <- Con función
prod_punto = ((v1[0]*v2[0]) + (v1[1]*v2[1]) + (v1[2]*v2[2])) # <- Paso a paso
print(f"Producto Punto: {prod_punto}")

# -> Producto Cruz:
cruz_x = (v1[1] * v2[2]) - (v1[2] * v2[1])
cruz_y = (v1[2] * v2[0]) - (v1[0] * v2[2])
cruz_z = (v1[0] * v2[1]) - (v1[1] * v2[0])

prod_cruz = np.array([cruz_x, cruz_y, cruz_z]) # <- Paso a paso
#prod_cruz = np.cross(v1, v2) # <- Con función 

print(f"Producto Cruz: {prod_cruz}")

# -> División:
division = v1 / v2
print(f"División: {division}")
