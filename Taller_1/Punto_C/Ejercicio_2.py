#2.Realice un programa que le permita al usuario ingresar los coeficientes de una función de transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Entrada de parámetros canónicos
wn = float(input("Frecuencia natural ωn: "))
zeta = float(input("Factor de amortiguamiento ζ: "))
K = float(input("Ganancia K: "))

# Función de transferencia en forma canónica
num = [K * wn**2]
den = [1, 2*zeta*wn, wn**2]

sistema = signal.TransferFunction(num, den)

# Respuesta al escalón
t, y = signal.step(sistema)

plt.plot(t, y)
plt.title("Respuesta al Escalón - Sistema de Segundo Orden")
plt.xlabel("Tiempo (s)")
plt.ylabel("Salida")
plt.grid()
plt.show()

# Clasificación del sistema
print("\nClasificación del sistema:")

if zeta < 1:
    print("Sistema Subamortiguado")
elif np.isclose(zeta, 1):
    print("Sistema Críticamente Amortiguado")
else:
    print("Sistema Sobreamortiguado")