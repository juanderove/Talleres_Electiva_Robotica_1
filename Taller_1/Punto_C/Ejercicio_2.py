"""2. Realice un programa que le permita al usuario ingresar los coeficientes de una función de
transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo
de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Entrada de coeficientes
a2 = float(input("Coeficiente de s^2: "))
a1 = float(input("Coeficiente de s: "))
a0 = float(input("Término independiente: "))
K = float(input("Ganancia K: "))

# Sistema
num = [K]
den = [a2, a1, a0]

sistema = signal.TransferFunction(num, den)

# Respuesta al escalón
t, y = signal.step(sistema)

plt.plot(t, y)
plt.title("Respuesta al Escalón - Sistema de Segundo Orden")
plt.xlabel("Tiempo (s)")
plt.ylabel("Salida")
plt.grid()
plt.show()

# Cálculo del amortiguamiento
wn = np.sqrt(a0/a2)
zeta = a1 / (2*np.sqrt(a0*a2))

print("\nFactor de amortiguamiento ζ =", round(zeta,4))

if zeta < 1:
    print("Sistema Subamortiguado")
elif zeta == 1:
    print("Sistema Críticamente Amortiguado")
else:
    print("Sistema Sobreamortiguado")