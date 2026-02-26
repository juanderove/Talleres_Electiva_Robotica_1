"""5. Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D, teniendo en cuenta
líneas rectas y/o curvas."""

import matplotlib.pyplot as plt
import numpy as np

# --- FUNCIÓN DE APOYO PARA CURVAS ---
def arco(x_centro, y_centro, radio, angulo_inicio, angulo_fin, offset):
    theta = np.linspace(angulo_inicio, angulo_fin, 50)
    x = radio * np.cos(theta) + x_centro + offset
    y = radio * np.sin(theta) + y_centro
    return x, y

# --- LETRAS COMPARTIDAS Y CORREGIDAS ---
def letra_I(offset, color="blue"): 
    plt.plot([0.5 + offset, 0.5 + offset], [0, 5], color=color, lw=3)

def letra_J(offset):
    plt.plot([1 + offset, 1 + offset], [0.5, 5], color="red", lw=3)
    x, y = arco(0.5, 0.5, 0.5, np.pi, 2*np.pi, offset)
    plt.plot(x, y, color="red", lw=3)
    plt.plot([0.5 + offset, 1.5 + offset], [5, 5], color="red", lw=3)

def letra_U(offset):
    plt.plot([0 + offset, 0 + offset], [0.5, 5], color="red", lw=3)
    plt.plot([1 + offset, 1 + offset], [0.5, 5], color="red", lw=3)
    x, y = arco(0.5, 0.5, 0.5, np.pi, 2*np.pi, offset)
    plt.plot(x, y, color="red", lw=3)

def letra_A(offset, color="red"):
    plt.plot([0 + offset, 0.5 + offset, 1 + offset], [0, 5, 0], color=color, lw=3)
    plt.plot([0.2 + offset, 0.8 + offset], [2, 2], color=color, lw=3)

def letra_N(offset):
    plt.plot([0 + offset, 0 + offset, 1 + offset, 1 + offset], [0, 5, 0, 5], color="red", lw=3)

def letra_W(offset):
    plt.plot([0+offset, 0.25+offset, 0.5+offset, 0.75+offset, 1+offset], [5, 0, 2.5, 0, 5], color="purple", lw=3)

def letra_L(offset):
    plt.plot([0+offset, 0+offset, 1+offset], [5, 0, 0], color="purple", lw=3)

def letra_M(offset):
    plt.plot([0+offset, 0+offset, 0.5+offset, 1+offset, 1+offset], [0, 5, 2.5, 5, 0], color="purple", lw=3)

def letra_R(offset):
    plt.plot([0+offset, 0+offset], [0, 5], color="purple", lw=3)
    x, y = arco(0, 3.5, 1.5, -np.pi/2, np.pi/2, offset)
    plt.plot(x, y, color="purple", lw=3)
    plt.plot([0+offset, 0.5+offset, 1+offset], [2, 1, 0], color="purple", lw=3)

def letra_D(offset):
    plt.plot([0+offset, 0+offset], [0, 5], color="blue", lw=3)
    x, y = arco(0, 2.5, 2.5, -np.pi/2, np.pi/2, offset)
    plt.plot(x, y, color="blue", lw=3)

def letra_V(offset):
    plt.plot([0+offset, 0.5+offset, 1+offset], [5, 0, 5], color="blue", lw=3)

# --- DIBUJO PRINCIPAL ---
plt.figure(figsize=(16, 5))

# JUAN
letra_J(0); letra_U(2); letra_A(4); letra_N(6)

# WILMAR (Offset 9 para separar de Juan)
letra_W(9); letra_I(10.5, "purple"); letra_L(12); letra_M(14); letra_A(16.5, "purple"); letra_R(18.5)

# DAVID (Offset 22 para separar de Wilmar)
letra_D(21); letra_A(24.5, "blue"); letra_V(26.5); letra_I(28); letra_D(29.5)

# Ajustes finales
plt.axis('equal')
plt.ylim(-1, 6)
plt.grid(True, linestyle=':', alpha=0.5)
plt.title("Integrantes: JUAN, WILMAR y DAVID", fontsize=14)
plt.show()