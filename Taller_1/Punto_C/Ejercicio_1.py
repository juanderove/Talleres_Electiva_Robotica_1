"""1. Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C."""

import numpy as np
import matplotlib.pyplot as plt

# Constantes PT100
R0 = 100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Rango de temperatura
T = np.linspace(-200, 200, 1000)

# Cálculo de resistencia
R = []

for temp in T:
    if temp >= 0:
        Rt = R0 * (1 + A*temp + B*(temp**2))
    else:
        Rt = R0 * (1 + A*temp + B*(temp**2) + C*(temp-100)*(temp**3))
    R.append(Rt)

# Gráfica
plt.plot(T, R)
plt.title("Comportamiento de la PT100")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Resistencia (Ohmios)")
plt.grid()
plt.show()