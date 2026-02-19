"""5. Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo)
y un parámetro de salida (matriz)."""

import math


def rotacion_x(angulo):
    theta = math.radians(angulo)
    Rx = [
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta),  math.cos(theta)]
    ]
    return Rx


def rotacion_y(angulo):
    theta = math.radians(angulo)
    Ry = [
        [ math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ]
    return Ry


def rotacion_z(angulo):
    theta = math.radians(angulo)
    Rz = [
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta),  math.cos(theta), 0],
        [0, 0, 1]
    ]
    return Rz


# Ángulo previamente definido 
angulo = 30

Rx = rotacion_x(angulo)
Ry = rotacion_y(angulo)
Rz = rotacion_z(angulo)

print("Rotación en X:")
for fila in Rx:
    print(fila)

print("\nRotación en Y:")
for fila in Ry:
    print(fila)

print("\nRotación en Z:")
for fila in Rz:
    print(fila)